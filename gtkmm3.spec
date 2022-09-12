#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gtkmm3
Version  : 3.24.7
Release  : 23
URL      : https://download.gnome.org/sources/gtkmm/3.24/gtkmm-3.24.7.tar.xz
Source0  : https://download.gnome.org/sources/gtkmm/3.24/gtkmm-3.24.7.tar.xz
Summary  : C++ binding for the GTK+ toolkit
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: gtkmm3-lib = %{version}-%{release}
Requires: gtkmm3-license = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : cairomm-dev
BuildRequires : compat-pangomm-soname14-dev
BuildRequires : doxygen
BuildRequires : pkgconfig(atkmm-1.6)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(mm-common-libstdc++)

%description
This is gtkmm, the C++ API for GTK.
See http://www.gtkmm.org/
# Building
Whenever possible, you should use the official binary packages approved by the
supplier of your operating system, such as your Linux distribution.

%package dev
Summary: dev components for the gtkmm3 package.
Group: Development
Requires: gtkmm3-lib = %{version}-%{release}
Provides: gtkmm3-devel = %{version}-%{release}
Requires: gtkmm3 = %{version}-%{release}

%description dev
dev components for the gtkmm3 package.


%package lib
Summary: lib components for the gtkmm3 package.
Group: Libraries
Requires: gtkmm3-license = %{version}-%{release}

%description lib
lib components for the gtkmm3 package.


%package license
Summary: license components for the gtkmm3 package.
Group: Default

%description license
license components for the gtkmm3 package.


%prep
%setup -q -n gtkmm-3.24.7
cd %{_builddir}/gtkmm-3.24.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1662991419
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check ||:

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gtkmm3
cp %{_builddir}/gtkmm-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gtkmm3/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
cp %{_builddir}/gtkmm-%{version}/COPYING.tools %{buildroot}/usr/share/package-licenses/gtkmm3/06877624ea5c77efe3b7e39b0f909eda6e25a4ec || :
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)
/usr/lib64/gtkmm-3.0/proc/m4/child_property.m4
/usr/lib64/gtkmm-3.0/proc/m4/class_gtkobject.m4
/usr/lib64/gtkmm-3.0/proc/m4/class_shared.m4
/usr/lib64/gtkmm-3.0/proc/m4/convert.m4
/usr/lib64/gtkmm-3.0/proc/m4/convert_gdk.m4
/usr/lib64/gtkmm-3.0/proc/m4/convert_gtk.m4
/usr/lib64/gtkmm-3.0/proc/m4/convert_gtkmm.m4

%files dev
%defattr(-,root,root,-)
/usr/include/gdkmm-3.0/gdkmm.h
/usr/include/gdkmm-3.0/gdkmm/applaunchcontext.h
/usr/include/gdkmm-3.0/gdkmm/color.h
/usr/include/gdkmm-3.0/gdkmm/cursor.h
/usr/include/gdkmm-3.0/gdkmm/device.h
/usr/include/gdkmm-3.0/gdkmm/devicemanager.h
/usr/include/gdkmm-3.0/gdkmm/display.h
/usr/include/gdkmm-3.0/gdkmm/displaymanager.h
/usr/include/gdkmm-3.0/gdkmm/dragcontext.h
/usr/include/gdkmm-3.0/gdkmm/drawingcontext.h
/usr/include/gdkmm-3.0/gdkmm/event.h
/usr/include/gdkmm-3.0/gdkmm/frameclock.h
/usr/include/gdkmm-3.0/gdkmm/frametimings.h
/usr/include/gdkmm-3.0/gdkmm/general.h
/usr/include/gdkmm-3.0/gdkmm/glcontext.h
/usr/include/gdkmm-3.0/gdkmm/monitor.h
/usr/include/gdkmm-3.0/gdkmm/pixbuf.h
/usr/include/gdkmm-3.0/gdkmm/pixbufanimation.h
/usr/include/gdkmm-3.0/gdkmm/pixbufanimationiter.h
/usr/include/gdkmm-3.0/gdkmm/pixbufformat.h
/usr/include/gdkmm-3.0/gdkmm/pixbufloader.h
/usr/include/gdkmm-3.0/gdkmm/private/applaunchcontext_p.h
/usr/include/gdkmm-3.0/gdkmm/private/color_p.h
/usr/include/gdkmm-3.0/gdkmm/private/cursor_p.h
/usr/include/gdkmm-3.0/gdkmm/private/device_p.h
/usr/include/gdkmm-3.0/gdkmm/private/devicemanager_p.h
/usr/include/gdkmm-3.0/gdkmm/private/display_p.h
/usr/include/gdkmm-3.0/gdkmm/private/displaymanager_p.h
/usr/include/gdkmm-3.0/gdkmm/private/dragcontext_p.h
/usr/include/gdkmm-3.0/gdkmm/private/drawingcontext_p.h
/usr/include/gdkmm-3.0/gdkmm/private/event_p.h
/usr/include/gdkmm-3.0/gdkmm/private/frameclock_p.h
/usr/include/gdkmm-3.0/gdkmm/private/frametimings_p.h
/usr/include/gdkmm-3.0/gdkmm/private/glcontext_p.h
/usr/include/gdkmm-3.0/gdkmm/private/monitor_p.h
/usr/include/gdkmm-3.0/gdkmm/private/pixbuf_p.h
/usr/include/gdkmm-3.0/gdkmm/private/pixbufanimation_p.h
/usr/include/gdkmm-3.0/gdkmm/private/pixbufanimationiter_p.h
/usr/include/gdkmm-3.0/gdkmm/private/pixbufformat_p.h
/usr/include/gdkmm-3.0/gdkmm/private/pixbufloader_p.h
/usr/include/gdkmm-3.0/gdkmm/private/rectangle_p.h
/usr/include/gdkmm-3.0/gdkmm/private/rgba_p.h
/usr/include/gdkmm-3.0/gdkmm/private/screen_p.h
/usr/include/gdkmm-3.0/gdkmm/private/seat_p.h
/usr/include/gdkmm-3.0/gdkmm/private/timecoord_p.h
/usr/include/gdkmm-3.0/gdkmm/private/types_p.h
/usr/include/gdkmm-3.0/gdkmm/private/visual_p.h
/usr/include/gdkmm-3.0/gdkmm/private/window_p.h
/usr/include/gdkmm-3.0/gdkmm/rectangle.h
/usr/include/gdkmm-3.0/gdkmm/rgba.h
/usr/include/gdkmm-3.0/gdkmm/screen.h
/usr/include/gdkmm-3.0/gdkmm/seat.h
/usr/include/gdkmm-3.0/gdkmm/timecoord.h
/usr/include/gdkmm-3.0/gdkmm/types.h
/usr/include/gdkmm-3.0/gdkmm/visual.h
/usr/include/gdkmm-3.0/gdkmm/window.h
/usr/include/gdkmm-3.0/gdkmm/wrap_init.h
/usr/include/gtkmm-3.0/gtkmm.h
/usr/include/gtkmm-3.0/gtkmm/aboutdialog.h
/usr/include/gtkmm-3.0/gtkmm/accelgroup.h
/usr/include/gtkmm-3.0/gtkmm/accelkey.h
/usr/include/gtkmm-3.0/gtkmm/accellabel.h
/usr/include/gtkmm-3.0/gtkmm/accelmap.h
/usr/include/gtkmm-3.0/gtkmm/action.h
/usr/include/gtkmm-3.0/gtkmm/actionable.h
/usr/include/gtkmm-3.0/gtkmm/actionbar.h
/usr/include/gtkmm-3.0/gtkmm/actiongroup.h
/usr/include/gtkmm-3.0/gtkmm/activatable.h
/usr/include/gtkmm-3.0/gtkmm/adjustment.h
/usr/include/gtkmm-3.0/gtkmm/alignment.h
/usr/include/gtkmm-3.0/gtkmm/appchooser.h
/usr/include/gtkmm-3.0/gtkmm/appchooserbutton.h
/usr/include/gtkmm-3.0/gtkmm/appchooserdialog.h
/usr/include/gtkmm-3.0/gtkmm/appchooserwidget.h
/usr/include/gtkmm-3.0/gtkmm/application.h
/usr/include/gtkmm-3.0/gtkmm/applicationwindow.h
/usr/include/gtkmm-3.0/gtkmm/arrow.h
/usr/include/gtkmm-3.0/gtkmm/aspectframe.h
/usr/include/gtkmm-3.0/gtkmm/assistant.h
/usr/include/gtkmm-3.0/gtkmm/base.h
/usr/include/gtkmm-3.0/gtkmm/bin.h
/usr/include/gtkmm-3.0/gtkmm/border.h
/usr/include/gtkmm-3.0/gtkmm/box.h
/usr/include/gtkmm-3.0/gtkmm/buildable.h
/usr/include/gtkmm-3.0/gtkmm/builder.h
/usr/include/gtkmm-3.0/gtkmm/button.h
/usr/include/gtkmm-3.0/gtkmm/buttonbox.h
/usr/include/gtkmm-3.0/gtkmm/calendar.h
/usr/include/gtkmm-3.0/gtkmm/cellarea.h
/usr/include/gtkmm-3.0/gtkmm/cellareabox.h
/usr/include/gtkmm-3.0/gtkmm/cellareacontext.h
/usr/include/gtkmm-3.0/gtkmm/celleditable.h
/usr/include/gtkmm-3.0/gtkmm/celllayout.h
/usr/include/gtkmm-3.0/gtkmm/cellrenderer.h
/usr/include/gtkmm-3.0/gtkmm/cellrenderer_generation.h
/usr/include/gtkmm-3.0/gtkmm/cellrendereraccel.h
/usr/include/gtkmm-3.0/gtkmm/cellrenderercombo.h
/usr/include/gtkmm-3.0/gtkmm/cellrendererpixbuf.h
/usr/include/gtkmm-3.0/gtkmm/cellrendererprogress.h
/usr/include/gtkmm-3.0/gtkmm/cellrendererspin.h
/usr/include/gtkmm-3.0/gtkmm/cellrendererspinner.h
/usr/include/gtkmm-3.0/gtkmm/cellrenderertext.h
/usr/include/gtkmm-3.0/gtkmm/cellrenderertoggle.h
/usr/include/gtkmm-3.0/gtkmm/cellview.h
/usr/include/gtkmm-3.0/gtkmm/checkbutton.h
/usr/include/gtkmm-3.0/gtkmm/checkmenuitem.h
/usr/include/gtkmm-3.0/gtkmm/childpropertyproxy.h
/usr/include/gtkmm-3.0/gtkmm/childpropertyproxy_base.h
/usr/include/gtkmm-3.0/gtkmm/clipboard.h
/usr/include/gtkmm-3.0/gtkmm/colorbutton.h
/usr/include/gtkmm-3.0/gtkmm/colorchooser.h
/usr/include/gtkmm-3.0/gtkmm/colorchooserdialog.h
/usr/include/gtkmm-3.0/gtkmm/colorselection.h
/usr/include/gtkmm-3.0/gtkmm/combobox.h
/usr/include/gtkmm-3.0/gtkmm/comboboxtext.h
/usr/include/gtkmm-3.0/gtkmm/container.h
/usr/include/gtkmm-3.0/gtkmm/cssprovider.h
/usr/include/gtkmm-3.0/gtkmm/csssection.h
/usr/include/gtkmm-3.0/gtkmm/dialog.h
/usr/include/gtkmm-3.0/gtkmm/drawingarea.h
/usr/include/gtkmm-3.0/gtkmm/editable.h
/usr/include/gtkmm-3.0/gtkmm/entry.h
/usr/include/gtkmm-3.0/gtkmm/entrybuffer.h
/usr/include/gtkmm-3.0/gtkmm/entrycompletion.h
/usr/include/gtkmm-3.0/gtkmm/enums.h
/usr/include/gtkmm-3.0/gtkmm/eventbox.h
/usr/include/gtkmm-3.0/gtkmm/eventcontroller.h
/usr/include/gtkmm-3.0/gtkmm/expander.h
/usr/include/gtkmm-3.0/gtkmm/filechooser.h
/usr/include/gtkmm-3.0/gtkmm/filechooserbutton.h
/usr/include/gtkmm-3.0/gtkmm/filechooserdialog.h
/usr/include/gtkmm-3.0/gtkmm/filechoosernative.h
/usr/include/gtkmm-3.0/gtkmm/filechooserwidget.h
/usr/include/gtkmm-3.0/gtkmm/filefilter.h
/usr/include/gtkmm-3.0/gtkmm/fixed.h
/usr/include/gtkmm-3.0/gtkmm/flowbox.h
/usr/include/gtkmm-3.0/gtkmm/flowboxchild.h
/usr/include/gtkmm-3.0/gtkmm/fontbutton.h
/usr/include/gtkmm-3.0/gtkmm/fontchooser.h
/usr/include/gtkmm-3.0/gtkmm/fontchooserdialog.h
/usr/include/gtkmm-3.0/gtkmm/fontchooserwidget.h
/usr/include/gtkmm-3.0/gtkmm/fontselection.h
/usr/include/gtkmm-3.0/gtkmm/frame.h
/usr/include/gtkmm-3.0/gtkmm/gesture.h
/usr/include/gtkmm-3.0/gtkmm/gesturedrag.h
/usr/include/gtkmm-3.0/gtkmm/gesturelongpress.h
/usr/include/gtkmm-3.0/gtkmm/gesturemultipress.h
/usr/include/gtkmm-3.0/gtkmm/gesturepan.h
/usr/include/gtkmm-3.0/gtkmm/gesturerotate.h
/usr/include/gtkmm-3.0/gtkmm/gesturesingle.h
/usr/include/gtkmm-3.0/gtkmm/gestureswipe.h
/usr/include/gtkmm-3.0/gtkmm/gesturezoom.h
/usr/include/gtkmm-3.0/gtkmm/glarea.h
/usr/include/gtkmm-3.0/gtkmm/grid.h
/usr/include/gtkmm-3.0/gtkmm/handlebox.h
/usr/include/gtkmm-3.0/gtkmm/headerbar.h
/usr/include/gtkmm-3.0/gtkmm/hvbox.h
/usr/include/gtkmm-3.0/gtkmm/hvbuttonbox.h
/usr/include/gtkmm-3.0/gtkmm/hvpaned.h
/usr/include/gtkmm-3.0/gtkmm/hvscale.h
/usr/include/gtkmm-3.0/gtkmm/hvscrollbar.h
/usr/include/gtkmm-3.0/gtkmm/hvseparator.h
/usr/include/gtkmm-3.0/gtkmm/iconfactory.h
/usr/include/gtkmm-3.0/gtkmm/iconinfo.h
/usr/include/gtkmm-3.0/gtkmm/iconset.h
/usr/include/gtkmm-3.0/gtkmm/iconsource.h
/usr/include/gtkmm-3.0/gtkmm/icontheme.h
/usr/include/gtkmm-3.0/gtkmm/iconview.h
/usr/include/gtkmm-3.0/gtkmm/image.h
/usr/include/gtkmm-3.0/gtkmm/imagemenuitem.h
/usr/include/gtkmm-3.0/gtkmm/infobar.h
/usr/include/gtkmm-3.0/gtkmm/invisible.h
/usr/include/gtkmm-3.0/gtkmm/label.h
/usr/include/gtkmm-3.0/gtkmm/layout.h
/usr/include/gtkmm-3.0/gtkmm/levelbar.h
/usr/include/gtkmm-3.0/gtkmm/linkbutton.h
/usr/include/gtkmm-3.0/gtkmm/listbox.h
/usr/include/gtkmm-3.0/gtkmm/listboxrow.h
/usr/include/gtkmm-3.0/gtkmm/liststore.h
/usr/include/gtkmm-3.0/gtkmm/listviewtext.h
/usr/include/gtkmm-3.0/gtkmm/lockbutton.h
/usr/include/gtkmm-3.0/gtkmm/main.h
/usr/include/gtkmm-3.0/gtkmm/menu.h
/usr/include/gtkmm-3.0/gtkmm/menubar.h
/usr/include/gtkmm-3.0/gtkmm/menubutton.h
/usr/include/gtkmm-3.0/gtkmm/menuitem.h
/usr/include/gtkmm-3.0/gtkmm/menushell.h
/usr/include/gtkmm-3.0/gtkmm/menutoolbutton.h
/usr/include/gtkmm-3.0/gtkmm/messagedialog.h
/usr/include/gtkmm-3.0/gtkmm/misc.h
/usr/include/gtkmm-3.0/gtkmm/modelbutton.h
/usr/include/gtkmm-3.0/gtkmm/nativedialog.h
/usr/include/gtkmm-3.0/gtkmm/notebook.h
/usr/include/gtkmm-3.0/gtkmm/numerableicon.h
/usr/include/gtkmm-3.0/gtkmm/object.h
/usr/include/gtkmm-3.0/gtkmm/offscreenwindow.h
/usr/include/gtkmm-3.0/gtkmm/orientable.h
/usr/include/gtkmm-3.0/gtkmm/overlay.h
/usr/include/gtkmm-3.0/gtkmm/pagesetup.h
/usr/include/gtkmm-3.0/gtkmm/pagesetupunixdialog.h
/usr/include/gtkmm-3.0/gtkmm/paned.h
/usr/include/gtkmm-3.0/gtkmm/papersize.h
/usr/include/gtkmm-3.0/gtkmm/placessidebar.h
/usr/include/gtkmm-3.0/gtkmm/plug.h
/usr/include/gtkmm-3.0/gtkmm/popover.h
/usr/include/gtkmm-3.0/gtkmm/popovermenu.h
/usr/include/gtkmm-3.0/gtkmm/printcontext.h
/usr/include/gtkmm-3.0/gtkmm/printer.h
/usr/include/gtkmm-3.0/gtkmm/printjob.h
/usr/include/gtkmm-3.0/gtkmm/printoperation.h
/usr/include/gtkmm-3.0/gtkmm/printoperationpreview.h
/usr/include/gtkmm-3.0/gtkmm/printsettings.h
/usr/include/gtkmm-3.0/gtkmm/printunixdialog.h
/usr/include/gtkmm-3.0/gtkmm/private/aboutdialog_p.h
/usr/include/gtkmm-3.0/gtkmm/private/accelgroup_p.h
/usr/include/gtkmm-3.0/gtkmm/private/accellabel_p.h
/usr/include/gtkmm-3.0/gtkmm/private/action_p.h
/usr/include/gtkmm-3.0/gtkmm/private/actionable_p.h
/usr/include/gtkmm-3.0/gtkmm/private/actionbar_p.h
/usr/include/gtkmm-3.0/gtkmm/private/actiongroup_p.h
/usr/include/gtkmm-3.0/gtkmm/private/activatable_p.h
/usr/include/gtkmm-3.0/gtkmm/private/adjustment_p.h
/usr/include/gtkmm-3.0/gtkmm/private/alignment_p.h
/usr/include/gtkmm-3.0/gtkmm/private/appchooser_p.h
/usr/include/gtkmm-3.0/gtkmm/private/appchooserbutton_p.h
/usr/include/gtkmm-3.0/gtkmm/private/appchooserdialog_p.h
/usr/include/gtkmm-3.0/gtkmm/private/appchooserwidget_p.h
/usr/include/gtkmm-3.0/gtkmm/private/application_p.h
/usr/include/gtkmm-3.0/gtkmm/private/applicationwindow_p.h
/usr/include/gtkmm-3.0/gtkmm/private/arrow_p.h
/usr/include/gtkmm-3.0/gtkmm/private/aspectframe_p.h
/usr/include/gtkmm-3.0/gtkmm/private/assistant_p.h
/usr/include/gtkmm-3.0/gtkmm/private/bin_p.h
/usr/include/gtkmm-3.0/gtkmm/private/border_p.h
/usr/include/gtkmm-3.0/gtkmm/private/box_p.h
/usr/include/gtkmm-3.0/gtkmm/private/buildable_p.h
/usr/include/gtkmm-3.0/gtkmm/private/builder_p.h
/usr/include/gtkmm-3.0/gtkmm/private/button_p.h
/usr/include/gtkmm-3.0/gtkmm/private/buttonbox_p.h
/usr/include/gtkmm-3.0/gtkmm/private/calendar_p.h
/usr/include/gtkmm-3.0/gtkmm/private/cellarea_p.h
/usr/include/gtkmm-3.0/gtkmm/private/cellareabox_p.h
/usr/include/gtkmm-3.0/gtkmm/private/cellareacontext_p.h
/usr/include/gtkmm-3.0/gtkmm/private/celleditable_p.h
/usr/include/gtkmm-3.0/gtkmm/private/celllayout_p.h
/usr/include/gtkmm-3.0/gtkmm/private/cellrenderer_p.h
/usr/include/gtkmm-3.0/gtkmm/private/cellrendereraccel_p.h
/usr/include/gtkmm-3.0/gtkmm/private/cellrenderercombo_p.h
/usr/include/gtkmm-3.0/gtkmm/private/cellrendererpixbuf_p.h
/usr/include/gtkmm-3.0/gtkmm/private/cellrendererprogress_p.h
/usr/include/gtkmm-3.0/gtkmm/private/cellrendererspin_p.h
/usr/include/gtkmm-3.0/gtkmm/private/cellrendererspinner_p.h
/usr/include/gtkmm-3.0/gtkmm/private/cellrenderertext_p.h
/usr/include/gtkmm-3.0/gtkmm/private/cellrenderertoggle_p.h
/usr/include/gtkmm-3.0/gtkmm/private/cellview_p.h
/usr/include/gtkmm-3.0/gtkmm/private/checkbutton_p.h
/usr/include/gtkmm-3.0/gtkmm/private/checkmenuitem_p.h
/usr/include/gtkmm-3.0/gtkmm/private/clipboard_p.h
/usr/include/gtkmm-3.0/gtkmm/private/colorbutton_p.h
/usr/include/gtkmm-3.0/gtkmm/private/colorchooser_p.h
/usr/include/gtkmm-3.0/gtkmm/private/colorchooserdialog_p.h
/usr/include/gtkmm-3.0/gtkmm/private/colorselection_p.h
/usr/include/gtkmm-3.0/gtkmm/private/combobox_p.h
/usr/include/gtkmm-3.0/gtkmm/private/comboboxtext_p.h
/usr/include/gtkmm-3.0/gtkmm/private/container_p.h
/usr/include/gtkmm-3.0/gtkmm/private/cssprovider_p.h
/usr/include/gtkmm-3.0/gtkmm/private/csssection_p.h
/usr/include/gtkmm-3.0/gtkmm/private/dialog_p.h
/usr/include/gtkmm-3.0/gtkmm/private/drawingarea_p.h
/usr/include/gtkmm-3.0/gtkmm/private/editable_p.h
/usr/include/gtkmm-3.0/gtkmm/private/entry_p.h
/usr/include/gtkmm-3.0/gtkmm/private/entrybuffer_p.h
/usr/include/gtkmm-3.0/gtkmm/private/entrycompletion_p.h
/usr/include/gtkmm-3.0/gtkmm/private/enums_p.h
/usr/include/gtkmm-3.0/gtkmm/private/eventbox_p.h
/usr/include/gtkmm-3.0/gtkmm/private/eventcontroller_p.h
/usr/include/gtkmm-3.0/gtkmm/private/expander_p.h
/usr/include/gtkmm-3.0/gtkmm/private/filechooser_p.h
/usr/include/gtkmm-3.0/gtkmm/private/filechooserbutton_p.h
/usr/include/gtkmm-3.0/gtkmm/private/filechooserdialog_p.h
/usr/include/gtkmm-3.0/gtkmm/private/filechoosernative_p.h
/usr/include/gtkmm-3.0/gtkmm/private/filechooserwidget_p.h
/usr/include/gtkmm-3.0/gtkmm/private/filefilter_p.h
/usr/include/gtkmm-3.0/gtkmm/private/fixed_p.h
/usr/include/gtkmm-3.0/gtkmm/private/flowbox_p.h
/usr/include/gtkmm-3.0/gtkmm/private/flowboxchild_p.h
/usr/include/gtkmm-3.0/gtkmm/private/fontbutton_p.h
/usr/include/gtkmm-3.0/gtkmm/private/fontchooser_p.h
/usr/include/gtkmm-3.0/gtkmm/private/fontchooserdialog_p.h
/usr/include/gtkmm-3.0/gtkmm/private/fontchooserwidget_p.h
/usr/include/gtkmm-3.0/gtkmm/private/fontselection_p.h
/usr/include/gtkmm-3.0/gtkmm/private/frame_p.h
/usr/include/gtkmm-3.0/gtkmm/private/gesture_p.h
/usr/include/gtkmm-3.0/gtkmm/private/gesturedrag_p.h
/usr/include/gtkmm-3.0/gtkmm/private/gesturelongpress_p.h
/usr/include/gtkmm-3.0/gtkmm/private/gesturemultipress_p.h
/usr/include/gtkmm-3.0/gtkmm/private/gesturepan_p.h
/usr/include/gtkmm-3.0/gtkmm/private/gesturerotate_p.h
/usr/include/gtkmm-3.0/gtkmm/private/gesturesingle_p.h
/usr/include/gtkmm-3.0/gtkmm/private/gestureswipe_p.h
/usr/include/gtkmm-3.0/gtkmm/private/gesturezoom_p.h
/usr/include/gtkmm-3.0/gtkmm/private/glarea_p.h
/usr/include/gtkmm-3.0/gtkmm/private/grid_p.h
/usr/include/gtkmm-3.0/gtkmm/private/handlebox_p.h
/usr/include/gtkmm-3.0/gtkmm/private/headerbar_p.h
/usr/include/gtkmm-3.0/gtkmm/private/hvbox_p.h
/usr/include/gtkmm-3.0/gtkmm/private/hvbuttonbox_p.h
/usr/include/gtkmm-3.0/gtkmm/private/hvpaned_p.h
/usr/include/gtkmm-3.0/gtkmm/private/hvscale_p.h
/usr/include/gtkmm-3.0/gtkmm/private/hvscrollbar_p.h
/usr/include/gtkmm-3.0/gtkmm/private/hvseparator_p.h
/usr/include/gtkmm-3.0/gtkmm/private/iconfactory_p.h
/usr/include/gtkmm-3.0/gtkmm/private/iconinfo_p.h
/usr/include/gtkmm-3.0/gtkmm/private/iconset_p.h
/usr/include/gtkmm-3.0/gtkmm/private/iconsource_p.h
/usr/include/gtkmm-3.0/gtkmm/private/icontheme_p.h
/usr/include/gtkmm-3.0/gtkmm/private/iconview_p.h
/usr/include/gtkmm-3.0/gtkmm/private/image_p.h
/usr/include/gtkmm-3.0/gtkmm/private/imagemenuitem_p.h
/usr/include/gtkmm-3.0/gtkmm/private/infobar_p.h
/usr/include/gtkmm-3.0/gtkmm/private/invisible_p.h
/usr/include/gtkmm-3.0/gtkmm/private/label_p.h
/usr/include/gtkmm-3.0/gtkmm/private/layout_p.h
/usr/include/gtkmm-3.0/gtkmm/private/levelbar_p.h
/usr/include/gtkmm-3.0/gtkmm/private/linkbutton_p.h
/usr/include/gtkmm-3.0/gtkmm/private/listbox_p.h
/usr/include/gtkmm-3.0/gtkmm/private/listboxrow_p.h
/usr/include/gtkmm-3.0/gtkmm/private/liststore_p.h
/usr/include/gtkmm-3.0/gtkmm/private/lockbutton_p.h
/usr/include/gtkmm-3.0/gtkmm/private/main_p.h
/usr/include/gtkmm-3.0/gtkmm/private/menu_p.h
/usr/include/gtkmm-3.0/gtkmm/private/menubar_p.h
/usr/include/gtkmm-3.0/gtkmm/private/menubutton_p.h
/usr/include/gtkmm-3.0/gtkmm/private/menuitem_p.h
/usr/include/gtkmm-3.0/gtkmm/private/menushell_p.h
/usr/include/gtkmm-3.0/gtkmm/private/menutoolbutton_p.h
/usr/include/gtkmm-3.0/gtkmm/private/messagedialog_p.h
/usr/include/gtkmm-3.0/gtkmm/private/misc_p.h
/usr/include/gtkmm-3.0/gtkmm/private/modelbutton_p.h
/usr/include/gtkmm-3.0/gtkmm/private/nativedialog_p.h
/usr/include/gtkmm-3.0/gtkmm/private/notebook_p.h
/usr/include/gtkmm-3.0/gtkmm/private/numerableicon_p.h
/usr/include/gtkmm-3.0/gtkmm/private/object_p.h
/usr/include/gtkmm-3.0/gtkmm/private/offscreenwindow_p.h
/usr/include/gtkmm-3.0/gtkmm/private/orientable_p.h
/usr/include/gtkmm-3.0/gtkmm/private/overlay_p.h
/usr/include/gtkmm-3.0/gtkmm/private/pagesetup_p.h
/usr/include/gtkmm-3.0/gtkmm/private/pagesetupunixdialog_p.h
/usr/include/gtkmm-3.0/gtkmm/private/paned_p.h
/usr/include/gtkmm-3.0/gtkmm/private/papersize_p.h
/usr/include/gtkmm-3.0/gtkmm/private/placessidebar_p.h
/usr/include/gtkmm-3.0/gtkmm/private/plug_p.h
/usr/include/gtkmm-3.0/gtkmm/private/popover_p.h
/usr/include/gtkmm-3.0/gtkmm/private/popovermenu_p.h
/usr/include/gtkmm-3.0/gtkmm/private/printcontext_p.h
/usr/include/gtkmm-3.0/gtkmm/private/printer_p.h
/usr/include/gtkmm-3.0/gtkmm/private/printjob_p.h
/usr/include/gtkmm-3.0/gtkmm/private/printoperation_p.h
/usr/include/gtkmm-3.0/gtkmm/private/printoperationpreview_p.h
/usr/include/gtkmm-3.0/gtkmm/private/printsettings_p.h
/usr/include/gtkmm-3.0/gtkmm/private/printunixdialog_p.h
/usr/include/gtkmm-3.0/gtkmm/private/progressbar_p.h
/usr/include/gtkmm-3.0/gtkmm/private/radioaction_p.h
/usr/include/gtkmm-3.0/gtkmm/private/radiobutton_p.h
/usr/include/gtkmm-3.0/gtkmm/private/radiomenuitem_p.h
/usr/include/gtkmm-3.0/gtkmm/private/radiotoolbutton_p.h
/usr/include/gtkmm-3.0/gtkmm/private/range_p.h
/usr/include/gtkmm-3.0/gtkmm/private/recentaction_p.h
/usr/include/gtkmm-3.0/gtkmm/private/recentchooser_p.h
/usr/include/gtkmm-3.0/gtkmm/private/recentchooserdialog_p.h
/usr/include/gtkmm-3.0/gtkmm/private/recentchoosermenu_p.h
/usr/include/gtkmm-3.0/gtkmm/private/recentchooserwidget_p.h
/usr/include/gtkmm-3.0/gtkmm/private/recentfilter_p.h
/usr/include/gtkmm-3.0/gtkmm/private/recentinfo_p.h
/usr/include/gtkmm-3.0/gtkmm/private/recentmanager_p.h
/usr/include/gtkmm-3.0/gtkmm/private/requisition_p.h
/usr/include/gtkmm-3.0/gtkmm/private/revealer_p.h
/usr/include/gtkmm-3.0/gtkmm/private/scale_p.h
/usr/include/gtkmm-3.0/gtkmm/private/scalebutton_p.h
/usr/include/gtkmm-3.0/gtkmm/private/scrollable_p.h
/usr/include/gtkmm-3.0/gtkmm/private/scrollbar_p.h
/usr/include/gtkmm-3.0/gtkmm/private/scrolledwindow_p.h
/usr/include/gtkmm-3.0/gtkmm/private/searchbar_p.h
/usr/include/gtkmm-3.0/gtkmm/private/searchentry_p.h
/usr/include/gtkmm-3.0/gtkmm/private/selectiondata_p.h
/usr/include/gtkmm-3.0/gtkmm/private/separator_p.h
/usr/include/gtkmm-3.0/gtkmm/private/separatormenuitem_p.h
/usr/include/gtkmm-3.0/gtkmm/private/separatortoolitem_p.h
/usr/include/gtkmm-3.0/gtkmm/private/settings_p.h
/usr/include/gtkmm-3.0/gtkmm/private/shortcutlabel_p.h
/usr/include/gtkmm-3.0/gtkmm/private/shortcutsgroup_p.h
/usr/include/gtkmm-3.0/gtkmm/private/shortcutssection_p.h
/usr/include/gtkmm-3.0/gtkmm/private/shortcutsshortcut_p.h
/usr/include/gtkmm-3.0/gtkmm/private/shortcutswindow_p.h
/usr/include/gtkmm-3.0/gtkmm/private/sizegroup_p.h
/usr/include/gtkmm-3.0/gtkmm/private/socket_p.h
/usr/include/gtkmm-3.0/gtkmm/private/spinbutton_p.h
/usr/include/gtkmm-3.0/gtkmm/private/spinner_p.h
/usr/include/gtkmm-3.0/gtkmm/private/stack_p.h
/usr/include/gtkmm-3.0/gtkmm/private/stacksidebar_p.h
/usr/include/gtkmm-3.0/gtkmm/private/stackswitcher_p.h
/usr/include/gtkmm-3.0/gtkmm/private/statusbar_p.h
/usr/include/gtkmm-3.0/gtkmm/private/statusicon_p.h
/usr/include/gtkmm-3.0/gtkmm/private/stockitem_p.h
/usr/include/gtkmm-3.0/gtkmm/private/stylecontext_p.h
/usr/include/gtkmm-3.0/gtkmm/private/styleprovider_p.h
/usr/include/gtkmm-3.0/gtkmm/private/switch_p.h
/usr/include/gtkmm-3.0/gtkmm/private/table_p.h
/usr/include/gtkmm-3.0/gtkmm/private/targetlist_p.h
/usr/include/gtkmm-3.0/gtkmm/private/tearoffmenuitem_p.h
/usr/include/gtkmm-3.0/gtkmm/private/textattributes_p.h
/usr/include/gtkmm-3.0/gtkmm/private/textbuffer_p.h
/usr/include/gtkmm-3.0/gtkmm/private/textchildanchor_p.h
/usr/include/gtkmm-3.0/gtkmm/private/textiter_p.h
/usr/include/gtkmm-3.0/gtkmm/private/textmark_p.h
/usr/include/gtkmm-3.0/gtkmm/private/texttag_p.h
/usr/include/gtkmm-3.0/gtkmm/private/texttagtable_p.h
/usr/include/gtkmm-3.0/gtkmm/private/textview_p.h
/usr/include/gtkmm-3.0/gtkmm/private/toggleaction_p.h
/usr/include/gtkmm-3.0/gtkmm/private/togglebutton_p.h
/usr/include/gtkmm-3.0/gtkmm/private/toggletoolbutton_p.h
/usr/include/gtkmm-3.0/gtkmm/private/toolbar_p.h
/usr/include/gtkmm-3.0/gtkmm/private/toolbutton_p.h
/usr/include/gtkmm-3.0/gtkmm/private/toolitem_p.h
/usr/include/gtkmm-3.0/gtkmm/private/toolitemgroup_p.h
/usr/include/gtkmm-3.0/gtkmm/private/toolpalette_p.h
/usr/include/gtkmm-3.0/gtkmm/private/toolshell_p.h
/usr/include/gtkmm-3.0/gtkmm/private/tooltip_p.h
/usr/include/gtkmm-3.0/gtkmm/private/treedragdest_p.h
/usr/include/gtkmm-3.0/gtkmm/private/treedragsource_p.h
/usr/include/gtkmm-3.0/gtkmm/private/treeiter_p.h
/usr/include/gtkmm-3.0/gtkmm/private/treemodel_p.h
/usr/include/gtkmm-3.0/gtkmm/private/treemodelfilter_p.h
/usr/include/gtkmm-3.0/gtkmm/private/treemodelsort_p.h
/usr/include/gtkmm-3.0/gtkmm/private/treepath_p.h
/usr/include/gtkmm-3.0/gtkmm/private/treerowreference_p.h
/usr/include/gtkmm-3.0/gtkmm/private/treeselection_p.h
/usr/include/gtkmm-3.0/gtkmm/private/treesortable_p.h
/usr/include/gtkmm-3.0/gtkmm/private/treestore_p.h
/usr/include/gtkmm-3.0/gtkmm/private/treeview_p.h
/usr/include/gtkmm-3.0/gtkmm/private/treeviewcolumn_p.h
/usr/include/gtkmm-3.0/gtkmm/private/uimanager_p.h
/usr/include/gtkmm-3.0/gtkmm/private/viewport_p.h
/usr/include/gtkmm-3.0/gtkmm/private/volumebutton_p.h
/usr/include/gtkmm-3.0/gtkmm/private/widget_p.h
/usr/include/gtkmm-3.0/gtkmm/private/widgetpath_p.h
/usr/include/gtkmm-3.0/gtkmm/private/window_p.h
/usr/include/gtkmm-3.0/gtkmm/private/windowgroup_p.h
/usr/include/gtkmm-3.0/gtkmm/progressbar.h
/usr/include/gtkmm-3.0/gtkmm/radioaction.h
/usr/include/gtkmm-3.0/gtkmm/radiobutton.h
/usr/include/gtkmm-3.0/gtkmm/radiobuttongroup.h
/usr/include/gtkmm-3.0/gtkmm/radiomenuitem.h
/usr/include/gtkmm-3.0/gtkmm/radiotoolbutton.h
/usr/include/gtkmm-3.0/gtkmm/range.h
/usr/include/gtkmm-3.0/gtkmm/recentaction.h
/usr/include/gtkmm-3.0/gtkmm/recentchooser.h
/usr/include/gtkmm-3.0/gtkmm/recentchooserdialog.h
/usr/include/gtkmm-3.0/gtkmm/recentchoosermenu.h
/usr/include/gtkmm-3.0/gtkmm/recentchooserwidget.h
/usr/include/gtkmm-3.0/gtkmm/recentfilter.h
/usr/include/gtkmm-3.0/gtkmm/recentinfo.h
/usr/include/gtkmm-3.0/gtkmm/recentmanager.h
/usr/include/gtkmm-3.0/gtkmm/requisition.h
/usr/include/gtkmm-3.0/gtkmm/revealer.h
/usr/include/gtkmm-3.0/gtkmm/scale.h
/usr/include/gtkmm-3.0/gtkmm/scalebutton.h
/usr/include/gtkmm-3.0/gtkmm/scrollable.h
/usr/include/gtkmm-3.0/gtkmm/scrollbar.h
/usr/include/gtkmm-3.0/gtkmm/scrolledwindow.h
/usr/include/gtkmm-3.0/gtkmm/searchbar.h
/usr/include/gtkmm-3.0/gtkmm/searchentry.h
/usr/include/gtkmm-3.0/gtkmm/selectiondata.h
/usr/include/gtkmm-3.0/gtkmm/selectiondata_private.h
/usr/include/gtkmm-3.0/gtkmm/separator.h
/usr/include/gtkmm-3.0/gtkmm/separatormenuitem.h
/usr/include/gtkmm-3.0/gtkmm/separatortoolitem.h
/usr/include/gtkmm-3.0/gtkmm/settings.h
/usr/include/gtkmm-3.0/gtkmm/shortcutlabel.h
/usr/include/gtkmm-3.0/gtkmm/shortcutsgroup.h
/usr/include/gtkmm-3.0/gtkmm/shortcutssection.h
/usr/include/gtkmm-3.0/gtkmm/shortcutsshortcut.h
/usr/include/gtkmm-3.0/gtkmm/shortcutswindow.h
/usr/include/gtkmm-3.0/gtkmm/sizegroup.h
/usr/include/gtkmm-3.0/gtkmm/socket.h
/usr/include/gtkmm-3.0/gtkmm/spinbutton.h
/usr/include/gtkmm-3.0/gtkmm/spinner.h
/usr/include/gtkmm-3.0/gtkmm/stack.h
/usr/include/gtkmm-3.0/gtkmm/stacksidebar.h
/usr/include/gtkmm-3.0/gtkmm/stackswitcher.h
/usr/include/gtkmm-3.0/gtkmm/statusbar.h
/usr/include/gtkmm-3.0/gtkmm/statusicon.h
/usr/include/gtkmm-3.0/gtkmm/stock.h
/usr/include/gtkmm-3.0/gtkmm/stockid.h
/usr/include/gtkmm-3.0/gtkmm/stockitem.h
/usr/include/gtkmm-3.0/gtkmm/stylecontext.h
/usr/include/gtkmm-3.0/gtkmm/styleproperty.h
/usr/include/gtkmm-3.0/gtkmm/styleprovider.h
/usr/include/gtkmm-3.0/gtkmm/switch.h
/usr/include/gtkmm-3.0/gtkmm/table.h
/usr/include/gtkmm-3.0/gtkmm/targetentry.h
/usr/include/gtkmm-3.0/gtkmm/targetlist.h
/usr/include/gtkmm-3.0/gtkmm/tearoffmenuitem.h
/usr/include/gtkmm-3.0/gtkmm/textattributes.h
/usr/include/gtkmm-3.0/gtkmm/textbuffer.h
/usr/include/gtkmm-3.0/gtkmm/textchildanchor.h
/usr/include/gtkmm-3.0/gtkmm/textiter.h
/usr/include/gtkmm-3.0/gtkmm/textmark.h
/usr/include/gtkmm-3.0/gtkmm/texttag.h
/usr/include/gtkmm-3.0/gtkmm/texttagtable.h
/usr/include/gtkmm-3.0/gtkmm/textview.h
/usr/include/gtkmm-3.0/gtkmm/toggleaction.h
/usr/include/gtkmm-3.0/gtkmm/togglebutton.h
/usr/include/gtkmm-3.0/gtkmm/toggletoolbutton.h
/usr/include/gtkmm-3.0/gtkmm/toolbar.h
/usr/include/gtkmm-3.0/gtkmm/toolbutton.h
/usr/include/gtkmm-3.0/gtkmm/toolitem.h
/usr/include/gtkmm-3.0/gtkmm/toolitemgroup.h
/usr/include/gtkmm-3.0/gtkmm/toolpalette.h
/usr/include/gtkmm-3.0/gtkmm/toolshell.h
/usr/include/gtkmm-3.0/gtkmm/tooltip.h
/usr/include/gtkmm-3.0/gtkmm/treedragdest.h
/usr/include/gtkmm-3.0/gtkmm/treedragsource.h
/usr/include/gtkmm-3.0/gtkmm/treeiter.h
/usr/include/gtkmm-3.0/gtkmm/treemodel.h
/usr/include/gtkmm-3.0/gtkmm/treemodelcolumn.h
/usr/include/gtkmm-3.0/gtkmm/treemodelfilter.h
/usr/include/gtkmm-3.0/gtkmm/treemodelsort.h
/usr/include/gtkmm-3.0/gtkmm/treepath.h
/usr/include/gtkmm-3.0/gtkmm/treerowreference.h
/usr/include/gtkmm-3.0/gtkmm/treeselection.h
/usr/include/gtkmm-3.0/gtkmm/treesortable.h
/usr/include/gtkmm-3.0/gtkmm/treestore.h
/usr/include/gtkmm-3.0/gtkmm/treeview.h
/usr/include/gtkmm-3.0/gtkmm/treeview_private.h
/usr/include/gtkmm-3.0/gtkmm/treeviewcolumn.h
/usr/include/gtkmm-3.0/gtkmm/uimanager.h
/usr/include/gtkmm-3.0/gtkmm/viewport.h
/usr/include/gtkmm-3.0/gtkmm/volumebutton.h
/usr/include/gtkmm-3.0/gtkmm/widget.h
/usr/include/gtkmm-3.0/gtkmm/widgetpath.h
/usr/include/gtkmm-3.0/gtkmm/window.h
/usr/include/gtkmm-3.0/gtkmm/windowgroup.h
/usr/include/gtkmm-3.0/gtkmm/wrap_init.h
/usr/lib64/gdkmm-3.0/include/gdkmmconfig.h
/usr/lib64/gtkmm-3.0/include/gtkmmconfig.h
/usr/lib64/libgdkmm-3.0.so
/usr/lib64/libgtkmm-3.0.so
/usr/lib64/pkgconfig/gdkmm-3.0.pc
/usr/lib64/pkgconfig/gtkmm-3.0.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgdkmm-3.0.so.1
/usr/lib64/libgdkmm-3.0.so.1.1.0
/usr/lib64/libgtkmm-3.0.so.1
/usr/lib64/libgtkmm-3.0.so.1.1.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gtkmm3/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/gtkmm3/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
