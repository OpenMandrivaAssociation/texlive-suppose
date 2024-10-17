Name:		texlive-suppose
Version:	59281
Release:	2
Summary:	Abbreviate the word "Suppose"
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/suppose
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/suppose.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/suppose.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides commands for abbreviating the word
"Suppose" in six fonts and with other variations. The author
recommends only using these commands when the immediately
succeeding strings are mathematical in nature. He does not
recommend using them in formal work. The package requires
amsmath, amsfonts, and graphicx.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/suppose
%doc %{_texmfdistdir}/doc/latex/suppose

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
