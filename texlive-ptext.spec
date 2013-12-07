# revision 30171
# category Package
# catalog-ctan /macros/xetex/latex/ptext
# catalog-date 2013-04-29 15:26:25 +0200
# catalog-license lppl1.2
# catalog-version 1.1
Name:		texlive-ptext
Version:	1.1
Release:	2
Summary:	A 'lipsum' for Persian
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/xetex/latex/ptext
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ptext.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ptext.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides lipsum-like facilities for the Persian
language. The source of the filling text is the Persian epic
"the Shanameh" (100 paragraphs are used.) The package needs to
be run under XeLaTeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/xelatex/ptext/ptext.sty
%doc %{_texmfdistdir}/doc/xelatex/ptext/README
%doc %{_texmfdistdir}/doc/xelatex/ptext/ptext.pdf
%doc %{_texmfdistdir}/doc/xelatex/ptext/ptext.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
