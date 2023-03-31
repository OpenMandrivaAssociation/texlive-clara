Name:		texlive-clara
Version:	54512
Release:	2
Summary:	A serif font family
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/clara
License:	ofl gpl2+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/clara.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/clara.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Clara is a type family created specially by Seamas O Brogain
for printing A Dictionary of Editing (2015). The family
includes italic, bold, bold italic, and small capitals, while
the character set includes (monotonic) Greek, Cyrillic, ogham,
phonetic and mathematical ranges, scribal abbreviations and
other specialist characters. The fonts also include some
OpenType features (such as ligature substitution, small
capitals, and old-style numerals) and variant forms for
particular languages.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/clara
%{_texmfdistdir}/fonts/vf/public/clara
%{_texmfdistdir}/fonts/type1/public/clara
%{_texmfdistdir}/fonts/tfm/public/clara
%{_texmfdistdir}/fonts/opentype/public/clara
%{_texmfdistdir}/fonts/map/dvips/clara
%{_texmfdistdir}/fonts/enc/dvips/clara
%doc %{_texmfdistdir}/doc/fonts/clara

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
