Name:		texlive-ptext
Version:	30171
Release:	2
Summary:	A 'lipsum' for Persian
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/ptext
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ptext.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ptext.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
