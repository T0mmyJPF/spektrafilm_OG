"""Presentation-only localization for the spektrafilm desktop GUI.

Enum values, profile identifiers, state keys, configuration data, and image data
remain unchanged. Set SPEKTRAFILM_LANGUAGE=en to restore the English UI.
"""
from __future__ import annotations
import os

_raw = os.environ.get("SPEKTRAFILM_LANGUAGE", "zh_CN").strip().lower()
LANGUAGE = "en" if _raw in {"en", "en_us", "english"} else "zh_CN"

_ZH = {
"main":"主界面","film":"胶片","print":"印相","advanced":"高级","config":"设置",
"napari layers":"图层","input":"输入","import raw":"导入 RAW","import rgb":"导入图像",
"crop and upscale":"裁剪与放大","spectral upsampling":"光谱上采样","profiles":"配置文件",
"camera":"相机","scanner":"扫描仪","display":"显示","experimental":"实验性功能","tune":"微调",
"halation":"光晕","grain":"颗粒","glare":"眩光","couplers":"成色剂","chemistry":"显影化学",
"preflash":"预闪光","diffusion":"柔化滤镜","input gamut compress":"输入色域压缩",
"output gamut compress":"输出色域压缩","gui parameters":"界面参数","exposure control":"曝光控制",
"enlarger":"放大机","output":"输出","white balance":"白平衡","temperature":"色温","tint":"色调",
"lens correction":"镜头校正","select file":"选择文件","no raw selected":"尚未选择 RAW 文件",
"no image selected":"尚未选择图像","reprocess raw":"重新处理 RAW",
"save current as default":"保存为默认设置","save current to file":"保存当前设置",
"load from file":"从文件加载","restore factory default":"恢复出厂默认设置",
"update":"更新","preview":"预览","scan":"扫描","save":"保存","ccw rotate":"逆时针旋转",
"cw rotate":"顺时针旋转","reset view":"重置视图","ready":"就绪",
"select input raw":"选择 RAW 输入文件","select input image":"选择输入图像",
"film profile":"胶片配置","print profile":"相纸配置","input color space":"输入色彩空间",
"output color space":"输出色彩空间","saving color space":"保存色彩空间",
"apply cctf decoding":"应用 CCTF 解码","saving cctf encoding":"保存时应用 CCTF 编码",
"upscale factor":"放大倍率","crop":"裁剪","crop center":"裁剪中心","crop size":"裁剪尺寸",
"spectral gaussian blur":"光谱高斯模糊","film channel swap":"胶片通道交换",
"print channel swap":"相纸通道交换","film gamma factor":"胶片伽马系数",
"use display transform":"使用显示变换","gray 18% canvas":"18% 灰背景","white padding":"白色边距",
"preview max size":"预览最大尺寸","output interpolation":"输出插值方式",
"print illuminant":"印相光源","print auto compensation":"自动补偿印相曝光",
"print exposure":"印相曝光","print y filter shift":"印相 Y 滤镜偏移",
"print m filter shift":"印相 M 滤镜偏移","auto preview":"自动预览","scan film":"扫描底片",
"scan for print":"印相扫描模式","gamma factor":"伽马系数","gamma factor fast":"快速层伽马系数",
"gamma factor slow":"慢速层伽马系数","gamma factor red":"红色通道伽马系数",
"gamma factor green":"绿色通道伽马系数","gamma factor blue":"蓝色通道伽马系数",
"developer exhaustion":"显影液疲劳","exposure":"曝光","y filter shift":"Y 滤镜偏移",
"m filter shift":"M 滤镜偏移","film format mm":"胶片画幅（mm）",
"lens blur um":"镜头模糊（μm）","auto exposure method":"自动曝光测光方式",
"auto exposure":"自动曝光","exposure compensation ev":"曝光补偿（EV）","lens blur":"镜头模糊",
"white correction":"白场校正","white level":"白场电平","black correction":"黑场校正",
"black level":"黑场电平","unsharp mask":"反锐化蒙版","algorithm":"算法","knee":"压缩拐点",
"active":"启用","amount":"强度","strength":"强度","spatial scale":"空间尺寸",
"scatter amount":"散射强度","scatter spatial scale":"散射范围","halation amount":"光晕强度",
"halation spatial scale":"光晕范围","boost ev":"高光提升（EV）","protect ev":"保护范围（EV）",
"boost range":"提升过渡范围","scatter core um":"散射核心（μm）","scatter tail um":"散射尾部（μm）",
"scatter tail weight":"散射尾部权重","halation strength":"光晕强度",
"halation first sigma um":"首轮光晕半径（μm）","halation n bounces":"光晕反射次数",
"halation bounce decay":"光晕衰减比例","halation renormalize":"保持中灰亮度",
"sublayers active":"启用分层颗粒","particle area um2":"颗粒面积（μm²）",
"particle scale":"颗粒尺寸倍率","particle scale layers":"子层颗粒倍率",
"density min":"最低密度","uniformity":"均匀度","blur":"模糊","blur dye clouds um":"染料云模糊（μm）",
"micro structure":"微观结构","percent":"比例","roughness":"粗糙度",
"preflash exposure":"预闪光曝光","preflash y filter shift":"预闪光 Y 滤镜偏移",
"preflash m filter shift":"预闪光 M 滤镜偏移","filter family":"滤镜类型","halo warmth":"光晕色温",
"core intensity":"核心强度","core size":"核心尺寸","halo intensity":"光晕强度",
"halo size":"光晕尺寸","bloom intensity":"泛光强度","bloom size":"泛光尺寸",
"as_shot":"拍摄时设置","daylight":"日光","tungsten":"钨丝灯","custom":"自定义",
"center_weighted":"中央重点测光","matrix":"矩阵测光","multi_zone":"多区测光",
"partial":"局部测光","highlight_weighted":"高光优先测光","median":"中值测光","average":"平均测光",
"nearest":"最近邻","linear":"线性","cubic":"三次插值","spline16":"样条 16",
"spline36":"样条 36","lanczos":"Lanczos","blackman":"Blackman",
"glimmerglass":"Glimmerglass","black_pro_mist":"Black Pro-Mist","pro_mist":"Pro-Mist",
"cinebloom":"CineBloom","xy":"CIE xy","oklch":"OKLCH","off":"关闭","aces_rgc":"ACES RGC",
"oklrab":"OKLab","jzazbz":"JzAzBz","cam16ucs":"CAM16-UCS",
"select white balance settings, if custom you can tune temperature and tint":"选择白平衡方式。选择“自定义”后，可以调整色温和色调。",
"temperature in kelvin for the custom whitebalance, not used for the other white balance settings":"自定义白平衡的色温，单位为 K。其他白平衡方式不会使用此参数。",
"tint value for the custom white balance, not used for the other white balance settings":"自定义白平衡的色调值。其他白平衡方式不会使用此参数。",
"apply lens corrections":"应用镜头校正。",
"enable dir coupler inhibition.":"启用 DIR 成色剂抑制效应。",
"enable halation and in-emulsion scatter.":"启用光晕和乳剂内部散射。",
"add grain to the negative":"为底片添加颗粒","add glare to the print":"为相纸添加眩光",
"enable print density-curve morphing.":"启用相纸密度曲线调整。",
"maximum highlight boost in stops.":"高光最大提升量，单位为档（stops）。",
"protected range above midgray for the boost onset in stops.":"高光提升开始生效前，在中灰以上保留的保护范围，单位为档。",
"controls how quickly the highlight boost ramps in, from 0 to 1.":"控制高光提升从 0 到 1 的渐进速度。",
"apply unsharp mask to the scan, [sigma in pixel, amount].":"对扫描结果应用反锐化蒙版，参数为 [像素 σ，强度]。",
"target white level applied when white correction is enabled.":"启用白场校正时使用的目标白场电平。",
"target black level applied when black correction is enabled.":"启用黑场校正时使用的目标黑场电平。",
"use neutral 18% gray as backgroung to judge the exposure and neutral colors":"使用中性 18% 灰作为背景，便于判断曝光和中性色。",
"max size of the long edge of the preview image in pixels":"预览图像长边的最大像素尺寸。",
"run the full simulation on the full-resolution input":"对完整分辨率的输入图像运行完整模拟。",
"save the current output layer to an image file":"将当前输出图层保存为图像文件。",
"pixel of the screen mapped 1 to 1 to the image pixel":"屏幕像素与图像像素按 1:1 映射显示。",
"2 screen pixels mapped to 1 image pixel":"2 个屏幕像素映射为 1 个图像像素。",
"4 screen pixels mapped to 1 image pixel":"4 个屏幕像素映射为 1 个图像像素。",
}

_ENUM_ZH = {
"as_shot":"拍摄时设置","daylight":"日光","tungsten":"钨丝灯","custom":"自定义",
"center_weighted":"中央重点测光","matrix":"矩阵测光","multi_zone":"多区测光",
"partial":"局部测光","highlight_weighted":"高光优先测光","median":"中值测光",
"average":"平均测光","nearest":"最近邻","linear":"线性","cubic":"三次插值",
"spline16":"样条 16","spline36":"样条 36","lanczos":"Lanczos","blackman":"Blackman",
"glimmerglass":"Glimmerglass","black_pro_mist":"Black Pro-Mist","pro_mist":"Pro-Mist",
"cinebloom":"CineBloom","xy":"CIE xy","oklch":"OKLCH","off":"关闭",
"aces_rgc":"ACES RGC","oklrab":"OKLab","jzazbz":"JzAzBz","cam16ucs":"CAM16-UCS",
}

def tr(text: str) -> str:
    if LANGUAGE == "en":
        return text
    key = " ".join(str(text).strip().split()).lower()
    return _ZH.get(key, text)

def enum_label(value: str) -> str:
    if LANGUAGE == "en":
        return value
    return _ENUM_ZH.get(value, value)

def tr_action(text: str) -> str:
    return text if LANGUAGE == "en" else tr(text.lower())
