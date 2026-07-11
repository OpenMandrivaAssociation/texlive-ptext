%global tl_name ptext
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	A lipsum for Persian
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/ptext
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ptext.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ptext.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides lipsum-like facilities for the Persian language.
The source of the filling text is the Persian epic "the Shanameh" (100
paragraphs are used.) The package needs to be run under XeLaTeX.

