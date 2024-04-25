Title: 在 Fedora 40 上配置 AMD ROCm 加速的 Stable Diffusion
Date: 2024-04-25 22:00
Category: Howto
Tags: fedora, amd, ai
Slug: configure-stable-diffusion-with-amd-rocm-on-fedora-40
Authors: lovenemesis

本文是[Fedora 39 上指南](https://linuxtoy.org/archives/configure-stable-diffusion-with-amd-rocm-on-fedora-39.html)的后续，同时附带了在升级过后需要注意的事项。

## 从 Fedora 39 升级至  Fedora 40 ##

由于 ROCm 6.0 相对 5.7 在打包依赖关系上的变化，可能需要在卸载了过往的部分 ROCm 包之后才能正常升级，比如笔者就遇到了必须先删除如下包才能运行升级：

`pkcon remove hipblas && pkcon remove hip-devel`

## 安装 AMD ROCm 计算框架 ##

[AMD 的 ROCm 计算框架](https://www.amd.com/en/products/software/rocm.html) 严格上来讲[仅支持少数几个面向企业的 Linux 发行版](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/tutorial/quick-start.html)，但得益于 Fedora 异构计算兴趣小组成员的努力，ROCm 框架中相当一部分软件包已经进入了 Fedora 的标准仓库中，截至本文发布时为 ROCm 6.0.2 版本。详细的步骤推荐参考[Fedora Wiki](https://fedoraproject.org/wiki/SIGs/HC)，这里简单说明下：

* 将当前用户添加到 `video` 组使得非 `root` 用户亦可使用显卡加速功能：`sudo usermod -a -G video $LOGNAME`
* 安装对应运行时环境、编译工具和辅助工具：`pkcon install rocminfo rocm-opencl rocm-hip rocm-smi`

这一步就完成了！由于 Fedora 38 之后的内核已经开启了 GPU 计算支持，这一步甚至比在官方支持的 Linux 发行版上安装还要简单。

此时可以尝试运行 `rocminfo` 确保显卡已经被 ROCm 框架正确识别。 

## 配置 Conda 安装 Python 3.11 ##

[Fedora 40 中默认预装的 Python 3.12](https://fedoraproject.org/wiki/Changes/Python3.12) 很可惜暂时还不被 [Stable Diffusion](https://stability.ai/stable-image) 支持，所以我们需要使用 [Conda](https://conda.io/) 创建一个使用 Python 3.11 的单独运行环境。所幸的是 Fedora 中已经收录了较新的 Conda 版本，直接从软件仓库安装配置即可：

* 从软件仓库安装：`pkcon install conda python3-pip`
* 创建使用 Python 3.11 的运行环境： `conda create -n py311 python=3.11 -y`
* 打开一个新的终端，启用刚刚创建的运行环境：`conda activate py311`

## 安装适用于 ROCm 的 PyTorch ##

虽说在上一部已经安装了底层运用的 PyTorch 框架，但这里我们需要安装其支持 ROCm 的版本，而又因为 Pytorch 尚未提供 Conda 版本的软件包，所以又需要使用 pip 安装。参考其[PyTorch 官方页面](https://pytorch.org/get-started/locally/)，在刚才**启用的 Python 3.11 环境**中，运行如下命令安装支持 ROCm 6.0 的稳定版本：

`pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm6.0`

如果是从 Fedora 39 升级上来的话，需要强制覆盖安装：

`pip3 install --force-reinstall torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm6.0`

这一步骤涉及约 2.4GB 的依赖安装，用时较长且需要稳定的网络环境。

## Stable Diffusion Web UI ##

[Stable Diffusion](https://stability.ai/stable-image) 流行的 [Stable Diffusion Web UI](https://github.com/AUTOMATIC1111/stable-diffusion-webui)的[一键式安装脚本](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Install-and-Run-on-AMD-GPUs)尚未支持 AMD 显卡在 Linux 系统下的安装，所以需要使用手动安装的方式。

* 下载其[发布版源代码包](https://github.com/AUTOMATIC1111/stable-diffusion-webui/releases)，本文发布时[为 1.9.3 版本](https://github.com/AUTOMATIC1111/stable-diffusion-webui/releases)。
* 解压并进入其目录：`tar xf stable-diffusion-webui-1.9.3.tar.gz && cd stable-diffusion-webui-1.9.3`
* 利用 pip 解决其依赖关系：`pip3 install -r requirements.txt`

这一步骤涉及约 4.5GB 的依赖安装，默认会下载 `v1-5-pruned-emaonly.safetensors` 版本的 checkpoint，用时较长且需要稳定的网络环境。

## 再次使用 ROCm 的 PyTorch 覆盖##

新版的 [Stable Diffusion Web UI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) 依赖关系会默认引入 NVIDIA CUDA 框架版本， 这里只需要使用 ROCm 的版本强制覆盖安装即可：

`pip3 install --force-reinstall torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm6.0`

由于 pip 的缓存机制，这一步并不消耗流量。

安装过后，建议参考[官网的验证过程](https://pytorch.org/get-started/locally/#linux-verification) 确保可以 PyTorch 正确识别到显卡加速支持。

至此安装步骤完成～

## 启动及运行 ##

启动和运行有几点需要注意的：

* 记得切换至 Python 3.11 环境：`conda activate py311`
* 目前**非 AMD ROCm 正式支持的显卡在运行时会遇到 [Bug](https://github.com/AUTOMATIC1111/stable-diffusion-webui/issues/15434)**，例如笔者游戏本上使用的 Radeon 780M，过往使用的覆盖环境变量如  `HSA_OVERRIDE_GFX_VERSION=11.0.0`不再有效
* 直接在 `stable-diffusion-webui-1.9.3` 目录下运行 `launch.py --listen` 即可
* 如果需要使用 WebUI 的插件支持的话，参照[其 Github Wiki](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Extensions) 添加运行时参数 `--enable-insecure-extension-access`
* 如果想用脚本方式将上述启动过程一次性整合到的话，可以使用 `conda run` 的方式，比如 `conda run -n py311 --live-stream python launch.py --listen --enable-insecure-extension-access`
* 更多的 Checkpoint 和 Refiner 可以[在 Hugging Face 找到](https://huggingface.co/stabilityai)。
* 工作的时候可以在另一个终端使用 `watch -n 1 -d rocm-smi` 监控 GPU 加速的运行状态。

## 法律声明 ##

使用过程中请[遵守 Stability AI 的使用条款](https://stability.ai/use-policy)并[尊重其他艺术家原创工作](https://stability.ai/s/Grassroots-innovation-in-open-models-suggested-amendments-to-the-AI-Act.pdf)，其结果切记**不可用于任何商业获利、歪曲事实、损害他人或违法所在国家法律的场景**。

## 参考 ##

* [AMD显卡满血Stable Diffusion无脑部署笔记](https://zhuanlan.zhihu.com/p/656480759)
* [How to use Stable Diffusion](https://stable-diffusion-art.com/beginners-guide/)

