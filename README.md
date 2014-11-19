eBot-API
========


APIs to interface with eBots

TOP view, with eBot upright
LED positions
left- Bluetooth
Centre- Charging
Right-MCU
---
title: Getting started with eBot 
description: eBot hardware and Soar code
author: Abhishek Gupta, Harsh Bhatt
tags: eBot, Soar, Edgebotix
created:  2014 Oct 20
modified: 2014 Nov 19

---
title: Getting started with eBot 
description: eBot hardware and Soar code
author: Abhishek Gupta, Harsh Bhatt
tags: eBot, Soar, Edgebotix
created:  2014 Oct 20
modified: 2014 Nov 19

---

Getting Started with eBot
=========

## eBot Description

[![solarized dualmode](https://github.com/altercation/solarized/raw/master/img/solarized-yinyang.png)](#features)

eBots are a robust, 3D-printed versatile STEM learning robotics platform that provide modularity and customization options. eBots aim to bridge the link between theory and practice by providing the ideal platform for students to collaborate and use their combined knowledge to build the best solution to a task. EdgeBotix wants to build the best supporting community and provide resources for teaching, making it extremely easy to integrate into the curriculum, something not seen in current educational robots.  

### Technical Specification

The following are detailed technical specifications of the eBots:
*	**Physical robot**
    *	15 x 15 x 8 cm, ABS plastic housing with various colour options
    *	Tank drive (2 drive treads)
        *	Powered by 2 low current Tamiya DC brushed motors
        *	150 RPM no load speed
        *	.2 m/s average speed
*	**Firmware**
    *	Powered by an ARM Cortex M0 microprocessor running at 48 MHz
*	**Sensors & other I/O**
    *	6 Sonar range finders (15 cm to 3 m range)
        *	1 Front facing
        *	2 At 45° from front
        *	2 Side facing
        *	1 Back facing
        *	Within 20 cm dead zone requirement
    *	6 DOF IMU (Accelerometer & Gyroscope)
        *	Raw acceleration data in x, y and z axis
        *	Raw euler angle (rotation) along x, y and z axis
    *	2 Encoders, providing distance and velocity measurements for both treads
    *	2 LDRs
        *	1 Top facing
        *	1 Front facing
    *	Onboard buzzer with a frequency range of 100 Hz to 10 KHz
*	**Wireless communication**
    *	Bluetooth connectivity to host computer
        *	Each robot has unique serialized Bluetooth identifier, in accordance to the serial number labeled on robot body
*	**Power**
    *	2 Ah Li-Po battery providing 3+ hours of continuous runtime
    *	Mini USB charging port
        *	1 Hour full charge time
*	**Software**
    *	eOS Running onboard eBots (an RTOS built on the mbed RTOS)
*	**Interface**
    * Currently there are two interface with python language
        *   [Soar Interface](#soar) 
        *   [API interface](#features)

### Pairing eBot
* eBot could be paired by entering the pairing code "0000". If you want the step by step guide of pairing with your system you can click [here](#detailed pairing).

### Python Installation
You might need:
* [Python 2.7](http://epd-free.enthought.com/?Download=Download+EPD+Free+7.3-2) 

Soar
---------
This section assumes that you have Python 2.7 already installed. 
To install Digital World Library, follow the steps according to your platform:
1.	OS X and Linux:
   * Download SOAR-master.zip from the [github](https://github.com/EdgeBotix/SOAR)
   * Open Terminal
   * Go the directory/folder where you save the file, e.g. if you save it to Mac's default Downloads folder, then type :
   ```
     cd $HOME/Downloads
    ```
   * Unzip the file, e.g. type :
   ```
      tar SOAR-master.zip
   ```
   * Go to the SOAR-master folder, e.g. type:
```    
  cd SOAR-master
   ```
   * Install the library by typing:
```   
   sudo python setup.py install
```
2.	Windows:
    * Download SOAR-master.zip from the [github](https://github.com/EdgeBotix/SOAR)
   * Unzip the file
   * Open Command Prompt by typing "cmd" from the Start Menu
   * Go the directory/folder where you have unzipped the file, e.g. type :
``` 
      cd C:\Downloads\SOAR-master\
   ``` 
   * Install the library by typing:
   ``` 
      python setup.py install
``` 


### RUNNING SIMULATOR - SOAR
After you have installed the Digital World Library, you can run the
simulator, called SOAR. To run it, follow the steps below:
1. OS X and Linux:
   * Open Terminal
   * Go to the SOAR-master folder
   * Go to soar folder
   * Run soar by typing: 
``` 
	python runsoar.py
``` 

2. Windows:
    * Open Command Prompt by typing "cmd" from the Start Menu
    * Go to the folder where you store Digital World Library, e.g.:
    ``` 
    cd C:\Downloads\SOAR-master\
    ``` 
    * Go to "soar" folder:
``` 
   cd soar
   ``` 
    * Run soar by typing:
    ``` 
    python runsoar.py
``` 

### USING SIMULATOR - SOAR
1. Running the code and connect to eBot using wireless connection:
   * Run Soar 
   * Click "Simulator" button to load any Python files for the "Worlds"
   * Click "Brain" button and choose the Python files containing your robot brain
   * Click "START" button to start connection with EBot

WORLD

Some World files for simulation has been created ans it is part of the Digital Library Package. It is also included in this package under the folder "worlds".

BRAIN

A simple Brain file has been included: brainfile.py.

* **Xresources** / Xdefaults
* **iTerm2**
* **OS X Terminal.app**
* **Putty** courtesy [Brant Bobby](http://www.control-v.net)
    and on [GitHub](https://github.com/brantb)
* **Xfce terminal** courtesy [Sasha Gerrand](http://sgerrand.com)
    and on [GitHub](https://github.com/sgerrand)

### Other Applications

*   **Mutt** e-mail client also by [me] (*just* the Mutt colorscheme is
    [available here][Mutt Repository])

### Palettes

* **Adobe Photoshop** Palette (inc. L\*a\*b values)
* **Apple Color Picker** Palettes
* **GIMP** Palette

Don't see the application you want to use it in? Download the palettes (or pull
the values from the table below) and create your own. Submit it back and I'll
happily note the contribution and include it on this page.  See also the
[Usage & Development](#usage-development) section below for details on the
specific values to be used in different contexts.

Download
--------

### [Click here to download latest version](http://ethanschoonover.com/solarized/files/solarized.zip)

Current release is **v1.0.0beta2**. See the [changelog] for details on what's
new in this release.

### Fresh Code on GitHub

You can also use the following links to access application specific downloads
and git repositories:

*   **Canonical Project Page:**

    Downloads, screenshots and more information are always available from the
    project page: <http://ethanschoonover.com/solarized>

*   **Full Git Repository:**

    The full git repository is at: <https://github.com/altercation/solarized>
    Get it using the following command:

        $ git clone git://github.com/altercation/solarized.git

*   **Application Specific Repositories:**

    You can clone repositories specific to many of the application specific
    color themes. See links in the list above or select from this list:

    * [Vim Repository]
    * [Mutt Repository]
    * [Emacs Repository]
    * [IntelliJ Repository]
    * [NetBeans Repository]
    * [SeeStyle-Coda-SubEthaEdit Repository]
    * [TextMate Repository]
    * [TextWrangler-BBEdit Repository]
    * [Visual Studio Repository]

    * [Xcode 3 work in progress][Xcode 3]
    * [Xcode 4 work in progress][Xcode 4]

Note that through the magic of [git-subtree](https://github.com/apenwarr/git-subtree)
these repositories are all kept in sync, so you can pull any of them and get the most up-to-date version.

Features
--------

1. **Selective contrast**

    On a sunny summer day I love to read a book outside. Not right in the sun;
    that's too bright. I'll hunt for a shady spot under a tree. The shaded
    paper contrasts with the crisp text nicely. If you were to actually measure
    the contrast between the two, you'd find it is much lower than black text
    on a white background (or white on black) on your display device of choice.
    Black text on white from a computer display is akin to reading a book in
    direct sunlight and tires the eye.

    ![solarized selective contrast](https://github.com/altercation/solarized/raw/master/img/solarized-selcon.png)

    Solarized reduces *brightness contrast* but, unlike many low contrast
    colorschemes, retains *contrasting hues* (based on colorwheel relations)
    for syntax highlighting readability.

2. **Both sides of the force**

    ![solarized dualmode](https://github.com/altercation/solarized/raw/master/img/solarized-dualmode.png)

    I often switch between dark and light modes when editing text and code.
    Solarized retains the same selective contrast relationships and overall
    feel when switching between the light and dark background modes. A *lot* of
    thought, planning and testing has gone into making both modes feel like
    part of a unified colorscheme.

3. **16/5 palette modes**

    ![solarized palettes](https://github.com/altercation/solarized/raw/master/img/solarized-165.png)

    Solarized works as a sixteen color palette for compatibility with common
    terminal based applications / emulators. In addition, it has been carefully
    designed to scale down to a variety of five color palettes (four base
    monotones plus one accent color) for use in design work such as web design.
    In every case it retains a strong personality but doesn't overwhelm.

5.  **Precision, symmetry**

    ![solarized symmetry](https://github.com/altercation/solarized/raw/master/img/solarized-sym.png)

    The monotones have symmetric CIELAB lightness differences, so switching
    from dark to light mode retains the same perceived contrast in brightness
    between each value. Each mode is equally readable. The accent colors are
    based off specific colorwheel relations and subsequently translated to
    CIELAB to ensure perceptual uniformity in terms of lightness. The hues
    themselves, as with the monotone \*a\*b values, have been adjusted within
    a small range to achieve the most pleasing combination of colors.

    See also the [Usage & Development](#usage-development) section below for
    details on the specific values to be used in different contexts.

    This makes colorscheme inversion trivial. Here, for instance, is a sass
    (scss) snippet that inverts solarized based on the class of the html tag
    (e.g. `<html class="dark red">` to give a dark background with red accent):

        $base03:    #002b36;
        $base02:    #073642;
        $base01:    #586e75;
        $base00:    #657b83;
        $base0:     #839496;
        $base1:     #93a1a1;
        $base2:     #eee8d5;
        $base3:     #fdf6e3;
        $yellow:    #b58900;
        $orange:    #cb4b16;
        $red:       #dc322f;
        $magenta:   #d33682;
        $violet:    #6c71c4;
        $blue:      #268bd2;
        $cyan:      #2aa198;
        $green:     #859900;
        @mixin rebase($rebase03,$rebase02,$rebase01,$rebase00,$rebase0,$rebase1,$rebase2,$rebase3)
        {
            background-color:$rebase03;
            color:$rebase0;
            * { color:$rebase0; }
            h1,h2,h3,h4,h5,h6 { color:$rebase1; border-color: $rebase0; }
            a, a:active, a:visited { color: $rebase1; }
        }
        @mixin accentize($accent) {
            a, a:active, a:visited, code.url { color: $accent; }
            h1,h2,h3,h4,h5,h6 {color:$accent}
        }
        /* light is default mode, so pair with general html definition */
        html, .light { @include rebase($base3,$base2,$base1,$base0,$base00,$base01,$base02,$base03)}
        .dark  { @include rebase($base03,$base02,$base01,$base00,$base0,$base1,$base2,$base3)}
        html * {
            color-profile: sRGB;
            rendering-intent: auto;
        }

    See also [the full css stylesheet for this site](https://github.com/altercation/ethanschoonover.com/blob/master/resources/css/style.css).

Installation
------------

Installation instructions for each version of the colorscheme are included in
the subdirectory README files. Note that for Vim (and possibly for Mutt) you
may want to clone the specific repository (for instance if you are using
Pathogen). See the links at the top of this file.

Font Samples
------------

Solarized has been designed to handle fonts of various weights and retain
readability, from the classic Terminus to the beefy Menlo.

![font samples - light](https://github.com/altercation/solarized/raw/master/img/solarized-fontsamples-light.png)
![font samples - dark](https://github.com/altercation/solarized/raw/master/img/solarized-fontsamples-dark.png)

Clockwise from upper left: Menlo, Letter Gothic, Terminus, Andale Mono.

Preview all code samples in specific font faces by selecting a link from this
list:

* [DejaVu Sans 18](http://ethanschoonover.com/solarized/img/dejavusans18/)
* [DejaVu Sans 14](http://ethanschoonover.com/solarized/img/dejavusans14/)
* [Letter Gothic 18](http://ethanschoonover.com/solarized/img/lettergothic18/)
* [Letter Gothic 14](http://ethanschoonover.com/solarized/img/lettergothic14/)

* [Andale Mono 14](http://ethanschoonover.com/solarized/img/andalemono14/)
* [Monaco 14](http://ethanschoonover.com/solarized/img/monaco14/)
* [Skyhook Mono 14](http://ethanschoonover.com/solarized/img/skyhookmono14/)

* [Terminus 12](http://ethanschoonover.com/solarized/img/terminus12/)
* [Terminus 20](http://ethanschoonover.com/solarized/img/terminus20/)

Screenshots
-----------

Click to view.

### Mutt

[![mutt dark](https://github.com/altercation/solarized/raw/master/img/screen-mutt-dark-th.png)](https://github.com/altercation/solarized/raw/master/img/screen-mutt-dark.png)
[![mutt light](https://github.com/altercation/solarized/raw/master/img/screen-mutt-light-th.png)](https://github.com/altercation/solarized/raw/master/img/screen-mutt-light.png)

### C (Vim)

[![c dark](https://github.com/altercation/solarized/raw/master/img/screen-c-dark-th.png)](https://github.com/altercation/solarized/raw/master/img/screen-c-dark.png)
[![c light](https://github.com/altercation/solarized/raw/master/img/screen-c-light-th.png)](https://github.com/altercation/solarized/raw/master/img/screen-c-light.png)

### Haskell (Vim)

[![haskell dark](https://github.com/altercation/solarized/raw/master/img/screen-haskell-dark-th.png)](https://github.com/altercation/solarized/raw/master/img/screen-haskell-dark.png)
[![haskell light](https://github.com/altercation/solarized/raw/master/img/screen-haskell-light-th.png)](https://github.com/altercation/solarized/raw/master/img/screen-haskell-light.png)

### HTML (Vim)

[![html dark](https://github.com/altercation/solarized/raw/master/img/screen-html-dark-th.png)](https://github.com/altercation/solarized/raw/master/img/screen-html-dark.png)
[![html light](https://github.com/altercation/solarized/raw/master/img/screen-html-light-th.png)](https://github.com/altercation/solarized/raw/master/img/screen-html-light.png)

### Java (Vim)

[![java dark](https://github.com/altercation/solarized/raw/master/img/screen-java-dark-th.png)](https://github.com/altercation/solarized/raw/master/img/screen-java-dark.png)
[![java light](https://github.com/altercation/solarized/raw/master/img/screen-java-light-th.png)](https://github.com/altercation/solarized/raw/master/img/screen-java-light.png)

### Javascript (Vim)

[![javascript dark](https://github.com/altercation/solarized/raw/master/img/screen-javascript-dark-th.png)](https://github.com/altercation/solarized/raw/master/img/screen-javascript-dark.png)
[![javascript light](https://github.com/altercation/solarized/raw/master/img/screen-javascript-light-th.png)](https://github.com/altercation/solarized/raw/master/img/screen-javascript-light.png)

### Pandoc Markdown (Vim)

These screen shots show Vim running with my own [Pandoc Kit Syntax](http://ethanschoonover.com/pandockit/).

[![pandoc dark](https://github.com/altercation/solarized/raw/master/img/screen-pandoc-dark-th.png)](https://github.com/altercation/solarized/raw/master/img/screen-pandoc-dark.png)
[![pandoc light](https://github.com/altercation/solarized/raw/master/img/screen-pandoc-light-th.png)](https://github.com/altercation/solarized/raw/master/img/screen-pandoc-light.png)

### Perl (Vim)

[![perl dark](https://github.com/altercation/solarized/raw/master/img/screen-perl-dark-th.png)](https://github.com/altercation/solarized/raw/master/img/screen-perl-dark.png)
[![perl light](https://github.com/altercation/solarized/raw/master/img/screen-perl-light-th.png)](https://github.com/altercation/solarized/raw/master/img/screen-perl-light.png)

### PHP (Vim)

[![php dark](https://github.com/altercation/solarized/raw/master/img/screen-php-dark-th.png)](https://github.com/altercation/solarized/raw/master/img/screen-php-dark.png)
[![php light](https://github.com/altercation/solarized/raw/master/img/screen-php-light-th.png)](https://github.com/altercation/solarized/raw/master/img/screen-php-light.png)

### Python (Vim)

[![python dark](https://github.com/altercation/solarized/raw/master/img/screen-python-dark-th.png)](https://github.com/altercation/solarized/raw/master/img/screen-python-dark.png)
[![python light](https://github.com/altercation/solarized/raw/master/img/screen-python-light-th.png)](https://github.com/altercation/solarized/raw/master/img/screen-python-light.png)

### Ruby (Vim)

[![ruby dark](https://github.com/altercation/solarized/raw/master/img/screen-ruby-dark-th.png)](https://github.com/altercation/solarized/raw/master/img/screen-ruby-dark.png)
[![ruby light](https://github.com/altercation/solarized/raw/master/img/screen-ruby-light-th.png)](https://github.com/altercation/solarized/raw/master/img/screen-ruby-light.png)

### Shell (Vim)

[![shell dark](https://github.com/altercation/solarized/raw/master/img/screen-shell-dark-th.png)](https://github.com/altercation/solarized/raw/master/img/screen-shell-dark.png)
[![shell light](https://github.com/altercation/solarized/raw/master/img/screen-shell-light-th.png)](https://github.com/altercation/solarized/raw/master/img/screen-shell-light.png)

### TeX (Vim)

[![tex dark](https://github.com/altercation/solarized/raw/master/img/screen-tex-dark-th.png)](https://github.com/altercation/solarized/raw/master/img/screen-tex-dark.png)
[![tex light](https://github.com/altercation/solarized/raw/master/img/screen-tex-light-th.png)](https://github.com/altercation/solarized/raw/master/img/screen-tex-light.png)

The Values
----------

L\*a\*b values are canonical (White D65, Reference D50), other values are
matched in sRGB space.

    SOLARIZED HEX     16/8 TERMCOL  XTERM/HEX   L*A*B      RGB         HSB
    --------- ------- ---- -------  ----------- ---------- ----------- -----------
    base03    #002b36  8/4 brblack  234 #1c1c1c 15 -12 -12   0  43  54 193 100  21
    base02    #073642  0/4 black    235 #262626 20 -12 -12   7  54  66 192  90  26
    base01    #586e75 10/7 brgreen  240 #585858 45 -07 -07  88 110 117 194  25  46
    base00    #657b83 11/7 bryellow 241 #626262 50 -07 -07 101 123 131 195  23  51
    base0     #839496 12/6 brblue   244 #808080 60 -06 -03 131 148 150 186  13  59
    base1     #93a1a1 14/4 brcyan   245 #8a8a8a 65 -05 -02 147 161 161 180   9  63
    base2     #eee8d5  7/7 white    254 #e4e4e4 92 -00  10 238 232 213  44  11  93
    base3     #fdf6e3 15/7 brwhite  230 #ffffd7 97  00  10 253 246 227  44  10  99
    yellow    #b58900  3/3 yellow   136 #af8700 60  10  65 181 137   0  45 100  71
    orange    #cb4b16  9/3 brred    166 #d75f00 50  50  55 203  75  22  18  89  80
    red       #dc322f  1/1 red      160 #d70000 50  65  45 220  50  47   1  79  86
    magenta   #d33682  5/5 magenta  125 #af005f 50  65 -05 211  54 130 331  74  83
    violet    #6c71c4 13/5 brmagenta 61 #5f5faf 50  15 -45 108 113 196 237  45  77
    blue      #268bd2  4/4 blue      33 #0087ff 55 -10 -45  38 139 210 205  82  82
    cyan      #2aa198  6/6 cyan      37 #00afaf 60 -35 -05  42 161 152 175  74  63
    green     #859900  2/2 green     64 #5f8700 60 -20  65 133 153   0  68 100  60

Usage & Development
-------------------

If you are considering developing a port for Solarized, please see also the
[developer notes](http://ethanschoonover.com/solarized/DEVELOPERS) for
information about optional repository structure and readme formats.

Solarized flips between light and dark modes. In each mode, four monotones form
the core values (with an optional fifth for emphasized content).

![value samples - dark](https://github.com/altercation/solarized/raw/master/img/solarized-values-dark.png)

![value samples - light](https://github.com/altercation/solarized/raw/master/img/solarized-values-light.png)

Thus in the case of a dark background colorscheme, the normal relationship for
background and body text is `base03:base0` (please note that body text is
**not** `base00`).  Note also that in cases where the background and foreground
can be specified as a pair value, text can be highlighted using a combination
of `base02:base1`. The L\*a\*b lightness difference between `base03:base0` and
`base02:base1` is identical by design, resulting in identical readability
against both normal and highlighted backgrounds. An example use case is folded
text in Vim which uses `base02` for the background and `base1` for the
foreground.

The values in this example are simply inverted in the case of a light
background.



[Vim Repository]: https://github.com/altercation/vim-colors-solarized
[Mutt Repository]: https://github.com/altercation/mutt-colors-solarized
[Emacs Repository]: https://github.com/sellout/emacs-color-theme-solarized
[IntelliJ Repository]: https://github.com/jkaving/intellij-colors-solarized
[NetBeans Repository]: https://github.com/fentie/netbeans-colors-solarized
[SeeStyle-Coda-SubEthaEdit Repository]: https://github.com/bobthecow/solarized-seestyle
[TextMate Repository]: https://github.com/deplorableword/textmate-solarized
[TextWrangler-BBEdit Repository]: https://github.com/rcarmo/textwrangler-bbedit-solarized
[Visual Studio Repository]: https://github.com/leddt/visualstudio-colors-solarized
[Xcode 3]: https://github.com/shayne/solarized/tree/master/apple-xcode3-solarized
[Xcode 4]: https://github.com/brianmichel/solarized/tree/master/apple-xcode4-solarized
[me]: http://ethanschoonover.com/colophon
[changelog]: http://ethanschoonover.com/solarized/CHANGELOG
[Vim README]: http://ethanschoonover.com/solarized/vim-colors-solarized
