#! /bin/sh

RED="\e[1;31m"
GREEN="\e[1;32m"
YELLOW="\e[1;33m"
BLUE="\e[1;34m"
ESC="\e[0m"

install_1() {
	pip install ./dist/ft_package-0.0.1.tar.gz
}

install_2(){
	pip install ./dist/ft_package-0.0.1-py3-none-any.whl
}

install_3() {
	pip uninstall ft_package
}

help(){
    echo "Want to install with 'ft_package-0.0.1.tar.gz'"
    echo "RUN : ${GREEN}${0} 1 ${ESC}"
	echo ""
    echo "Want to install with 'ft_package-0.0.1-py3-none-any.whl'"
    echo "RUN : ${GREEN}${0} 2 ${ESC}"
	echo ""
    echo "Want to uninstall 'ft_package' ?"
    echo "RUN : ${GREEN}${0} 3 ${ESC}"
}


if [ -z "$1" ] ; then
    help
	exit 1
fi

if [ "$1" != "1" ] && [ "$1" != "2" ] && [ "$1" != "3" ] ; then
    echo "${RED}Incorrect arguments provided ${ESC}"
    help
	exit 1
fi

if [ "$1" = "1" ] ; then
	install_1
	exit 1
fi

if [ "$1" = "2" ] ; then
	install_2
	exit 1
fi

if [ "$1" = "3" ] ; then
	install_3
	exit 1
fi
