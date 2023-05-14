# x1pcgconv

x1pcgconvは、任意の画像をX1のPCGフォーマットに変換して出力するための画像コンバータです。

## Install

```
pip install git+https://github.com/h-o-soft/x1pcgconv
```

## Usage

```
x1pcgconv SHARP X1 PCG converter Version 0.1.0 Copyright 2023 H.O SOFT Inc.

positional arguments:
  path                  file path(s)

optional arguments:
  -h, --help            show this help message and exit
  -f, --force           set force write
  -m {reduce,dither,edfs,retro}, --mode {reduce,dither,edfs,retro}
                        convert mode (default = reduce)
  -g, --gamma           fixed gamma (default = disable)
  -p, --png             output png file (default = disable)
  -s RESIZE, --resize RESIZE
                        resize image (ex. 128x128) (default = disable)
  -S SATURATION, --saturation SATURATION
                        saturation (effective only in retro mode / default = None)
  -n NORMAL, --normal NORMAL
                        normal order (normal PCG order/ default = x3 order)
```

### PCG形式への変換

```
x1pcgconv image-file-path
```

または

```
x1pcgconv image-file-path output-file-path
```

パス名を1つだけ引数に指定すると、そのファイル名の拡張子を「pcg」に変更して出力します。また、明示的に出力ファイル名を渡すと、そのパスに出力します。

既に画像ファイルがある場合は上書きされませんので、上書きしたい場合はオプション「-f」をつけてください。

### 強制上書き

```
x1pcgconv -f image-file-path
```

`-f` オプションをつけると、出力先ファイルが既に存在していても上書きします。

指定しない場合、上書きを行わないので注意してください(常に指定しておいてもいいかもしれません)。

### リサイズ

```
x1pcgconv -s 128x128 image-file-path
```

`-s` オプションに (横サイズ)x(縦サイズ) を指定する事で、画像をリサイズしてから変換します。

アスペクト比に関わらず指定サイズになりますが、画像のアスペクト比は維持されます。

また、縦、横ともに8の倍数である必要があります。

### ガンマ補正

```
x1pcgconv -g image-file-path
```

`-g` オプションをつけると、ガンマ補正をかけて出力します。

### 減色モードの指定

```
x1pcgconv -m (減色モード) image-file-path
```

減色モードを指定する事で、いくつかの形式で減色したものをM8Aファイルとして出力します。

指定可能なモードは下記のとおりです。

* reduce
  * 単純な8色への変換を行います
* dither
  * 4x4の配列ディザ変換を行います
* edfs
  * 誤差拡散法での変換を行います(error diffusion / Floyd & Steinberg)
* retro
  * なんとなくレトロっぽい彩度高めのディザ変換を行います
  * デイリーポータルZの記事「[レトロPCゲームみたいな写真が撮りたい](https://dailyportalz.jp/kiji/retro_PC_game-mitaina-shashin)」の変換を参考にしています(ありがとうございます)

### 彩度の指定

```
x1pcgconv -S 2.0 image-file-path
```

減色モード「retro」の時のみ、画像の彩度を設定出来ます。

デフォルト値は 2.0 になります。

### 三倍速定義及び通常定義の指定

-n オプションをつけないと、三倍速定義モードの配列でPCGデータを出力します。

-n オプションをつけると、通常のX1のPCG配列でデータを出力します(が、未検証なので間違っている気がします)。

SLANG-compilerのPCGDEF関数では三倍速定義フォーマットを定義するので、SLANG-compilerで使う場合は -n オプションをつけないようにしてください。

### 減色の例
M8A形式へのコンバータ m8acnv と同様なので、そちらを参照してください

https://github.com/h-o-soft/m8acnv

## pngファイルの出力

通常はPCGフォーマットのファイルのみ出力しますが、 `-p` オプションをつける事で、pcgファイルの末尾に「.png」を付与したpngファイルも同時に出力します。

変換後のイメージを事前に確認したい時にお使いください。

## 謝辞

reduce、dither、edfsの変換については、 hex125(293) 氏のHSPのコードを元にして実装しました。ありがとうございます。

retro変換については斎藤公輔（NEKOPLA）氏によるImageMagickのオプションを元に実装しました。ありがとうございます。

## Author
* OGINO Hiroshi
* H.O SOFT Inc.
* twitter: @honda_ken

## License
"x1pcgconv" is under [MIT license](LICENSE)


