%global tl_name suppose
%global tl_revision 59281

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2.2
Release:	%{tl_revision}.1
Summary:	Abbreviate the word Suppose
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/suppose
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/suppose.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/suppose.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides commands for abbreviating the word "Suppose" in
six fonts and with other variations. The author recommends only using
these commands when the immediately succeeding strings are mathematical
in nature. He does not recommend using them in formal work. The package
requires amsmath, amsfonts, and graphicx.

