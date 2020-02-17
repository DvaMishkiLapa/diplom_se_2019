#!/bin/bash

distr=`awk 'NR==1 {print $1}' /etc/*-release`
if [[ "$distr" == "DISTRIB_ID=Ubuntu" ]]; then
    echo "############ Ubuntu detected ############"
    echo "############ Install texlive-bibtex-extra ############"
    sudo apt install texlive-bibtex-extra
    echo "############ Install biber ############"
    sudo apt install biber
    echo "############ Install cm-super ############"
    sudo apt install cm-super
    echo "############ Install texlive-lang-cyrillic ############"
    sudo apt install texlive-lang-cyrillic
    echo "############ Install texlive-fonts-recommended ############"
    sudo apt-get install texlive-fonts-recommended
    echo "############ Install libreoffice ############"
    sudo apt install libreoffice
else
    echo "############           Your distribution is not Ubuntu!         ############"
    echo "############ Find the following packages for your distribution: ############"
    echo "############      1. texlive-bibtex-extra or bibtex             ############"
    echo "############      2. biber                                      ############"
    echo "############      3. cm-super                                   ############"
    echo "############      4. texlive-lang-cyrillic                      ############"
    echo "############      5. install texlive-fonts-recommended          ############"
    echo "############      6. libreoffice                                ############"
fi
