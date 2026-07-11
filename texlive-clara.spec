%global tl_name clara
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A serif font family
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/clara
License:	ofl gpl2+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/clara.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/clara.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Clara is a type family created specially by Seamas O Brogain for
printing A Dictionary of Editing (2015). The family includes italic,
bold, bold italic, and small capitals, while the character set includes
(monotonic) Greek, Cyrillic, ogham, phonetic and mathematical ranges,
scribal abbreviations and other specialist characters. The fonts also
include some OpenType features (such as ligature substitution, small
capitals, and old-style numerals) and variant forms for particular
languages.

