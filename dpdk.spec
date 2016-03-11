#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dpdk
Version  : 2.2.0
Release  : 25
URL      : http://dpdk.org/browse/dpdk/snapshot/dpdk-2.2.0.tar.gz
Source0  : http://dpdk.org/browse/dpdk/snapshot/dpdk-2.2.0.tar.gz
Summary  : Data Plane Development Kit core
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause GPL-2.0 LGPL-2.0 LGPL-2.1
Requires: dpdk-bin
Requires: dpdk-lib
Requires: dpdk-data
BuildRequires : libpcap-dev
Patch1: 0001-disable-dpdk-kernel-modules.patch
Patch2: 0002-enable-dpdk-shared-libs.patch
Patch3: 0003-fix-conflicted-shebang-path-with-FHS.patch
Patch4: 0004-enable-combine-libs.patch
Patch5: 0005-fix-combined-shared-library-ABI-version.patch

%description
DPDK core includes kernel modules, core libraries and tools.
testpmd application allows to test fast packet processing environments
on x86 platforms. For instance, it can be used to check that environment
can support fast path applications such as 6WINDGate, pktgen, rumptcpip, etc.
More libraries are available as extensions in other packages.

%package bin
Summary: bin components for the dpdk package.
Group: Binaries
Requires: dpdk-data

%description bin
bin components for the dpdk package.


%package data
Summary: data components for the dpdk package.
Group: Data

%description data
data components for the dpdk package.


%package dev
Summary: dev components for the dpdk package.
Group: Development
Requires: dpdk-lib
Requires: dpdk-bin
Requires: dpdk-data
Provides: dpdk-devel

%description dev
dev components for the dpdk package.


%package lib
Summary: lib components for the dpdk package.
Group: Libraries
Requires: dpdk-data

%description lib
lib components for the dpdk package.


%prep
%setup -q -n dpdk-2.2.0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
make V=1  %{?_smp_mflags} config T=x86_64-native-linuxapp-gcc; make

%install
rm -rf %{buildroot}
%make_install prefix=/usr libdir=/usr/lib64 includedir=/usr/include

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dpdk_nic_bind
/usr/bin/dpdk_proc_info
/usr/bin/testpmd

%files data
%defattr(-,root,root,-)
/usr/share/dpdk/examples/Makefile
/usr/share/dpdk/examples/bond/Makefile
/usr/share/dpdk/examples/bond/main.c
/usr/share/dpdk/examples/bond/main.h
/usr/share/dpdk/examples/cmdline/Makefile
/usr/share/dpdk/examples/cmdline/commands.c
/usr/share/dpdk/examples/cmdline/commands.h
/usr/share/dpdk/examples/cmdline/main.c
/usr/share/dpdk/examples/cmdline/parse_obj_list.c
/usr/share/dpdk/examples/cmdline/parse_obj_list.h
/usr/share/dpdk/examples/distributor/Makefile
/usr/share/dpdk/examples/distributor/main.c
/usr/share/dpdk/examples/dpdk_qat/Makefile
/usr/share/dpdk/examples/dpdk_qat/config_files/coleto/dh895xcc_qa_dev0.conf
/usr/share/dpdk/examples/dpdk_qat/config_files/shumway/dh89xxcc_qa_dev0.conf
/usr/share/dpdk/examples/dpdk_qat/config_files/shumway/dh89xxcc_qa_dev1.conf
/usr/share/dpdk/examples/dpdk_qat/config_files/stargo/dh89xxcc_qa_dev0.conf
/usr/share/dpdk/examples/dpdk_qat/crypto.c
/usr/share/dpdk/examples/dpdk_qat/crypto.h
/usr/share/dpdk/examples/dpdk_qat/main.c
/usr/share/dpdk/examples/ethtool/Makefile
/usr/share/dpdk/examples/ethtool/ethtool-app/Makefile
/usr/share/dpdk/examples/ethtool/ethtool-app/ethapp.c
/usr/share/dpdk/examples/ethtool/ethtool-app/ethapp.h
/usr/share/dpdk/examples/ethtool/ethtool-app/main.c
/usr/share/dpdk/examples/ethtool/lib/Makefile
/usr/share/dpdk/examples/ethtool/lib/rte_ethtool.c
/usr/share/dpdk/examples/ethtool/lib/rte_ethtool.h
/usr/share/dpdk/examples/exception_path/Makefile
/usr/share/dpdk/examples/exception_path/main.c
/usr/share/dpdk/examples/helloworld/Makefile
/usr/share/dpdk/examples/helloworld/main.c
/usr/share/dpdk/examples/ip_fragmentation/Makefile
/usr/share/dpdk/examples/ip_fragmentation/main.c
/usr/share/dpdk/examples/ip_pipeline/Makefile
/usr/share/dpdk/examples/ip_pipeline/app.h
/usr/share/dpdk/examples/ip_pipeline/config/edge_router_downstream.cfg
/usr/share/dpdk/examples/ip_pipeline/config/edge_router_downstream.sh
/usr/share/dpdk/examples/ip_pipeline/config/edge_router_upstream.cfg
/usr/share/dpdk/examples/ip_pipeline/config/edge_router_upstream.sh
/usr/share/dpdk/examples/ip_pipeline/config/ip_pipeline.cfg
/usr/share/dpdk/examples/ip_pipeline/config/ip_pipeline.sh
/usr/share/dpdk/examples/ip_pipeline/config/l2fwd.cfg
/usr/share/dpdk/examples/ip_pipeline/config/l3fwd.cfg
/usr/share/dpdk/examples/ip_pipeline/config/l3fwd.sh
/usr/share/dpdk/examples/ip_pipeline/config/tm_profile.cfg
/usr/share/dpdk/examples/ip_pipeline/config_check.c
/usr/share/dpdk/examples/ip_pipeline/config_parse.c
/usr/share/dpdk/examples/ip_pipeline/config_parse_tm.c
/usr/share/dpdk/examples/ip_pipeline/cpu_core_map.c
/usr/share/dpdk/examples/ip_pipeline/cpu_core_map.h
/usr/share/dpdk/examples/ip_pipeline/init.c
/usr/share/dpdk/examples/ip_pipeline/main.c
/usr/share/dpdk/examples/ip_pipeline/pipeline.h
/usr/share/dpdk/examples/ip_pipeline/pipeline/hash_func.h
/usr/share/dpdk/examples/ip_pipeline/pipeline/pipeline_actions_common.h
/usr/share/dpdk/examples/ip_pipeline/pipeline/pipeline_common_be.c
/usr/share/dpdk/examples/ip_pipeline/pipeline/pipeline_common_be.h
/usr/share/dpdk/examples/ip_pipeline/pipeline/pipeline_common_fe.c
/usr/share/dpdk/examples/ip_pipeline/pipeline/pipeline_common_fe.h
/usr/share/dpdk/examples/ip_pipeline/pipeline/pipeline_firewall.c
/usr/share/dpdk/examples/ip_pipeline/pipeline/pipeline_firewall.h
/usr/share/dpdk/examples/ip_pipeline/pipeline/pipeline_firewall_be.c
/usr/share/dpdk/examples/ip_pipeline/pipeline/pipeline_firewall_be.h
/usr/share/dpdk/examples/ip_pipeline/pipeline/pipeline_flow_actions.c
/usr/share/dpdk/examples/ip_pipeline/pipeline/pipeline_flow_actions.h
/usr/share/dpdk/examples/ip_pipeline/pipeline/pipeline_flow_actions_be.c
/usr/share/dpdk/examples/ip_pipeline/pipeline/pipeline_flow_actions_be.h
/usr/share/dpdk/examples/ip_pipeline/pipeline/pipeline_flow_classification.c
/usr/share/dpdk/examples/ip_pipeline/pipeline/pipeline_flow_classification.h
/usr/share/dpdk/examples/ip_pipeline/pipeline/pipeline_flow_classification_be.c
/usr/share/dpdk/examples/ip_pipeline/pipeline/pipeline_flow_classification_be.h
/usr/share/dpdk/examples/ip_pipeline/pipeline/pipeline_master.c
/usr/share/dpdk/examples/ip_pipeline/pipeline/pipeline_master.h
/usr/share/dpdk/examples/ip_pipeline/pipeline/pipeline_master_be.c
/usr/share/dpdk/examples/ip_pipeline/pipeline/pipeline_master_be.h
/usr/share/dpdk/examples/ip_pipeline/pipeline/pipeline_passthrough.c
/usr/share/dpdk/examples/ip_pipeline/pipeline/pipeline_passthrough.h
/usr/share/dpdk/examples/ip_pipeline/pipeline/pipeline_passthrough_be.c
/usr/share/dpdk/examples/ip_pipeline/pipeline/pipeline_passthrough_be.h
/usr/share/dpdk/examples/ip_pipeline/pipeline/pipeline_routing.c
/usr/share/dpdk/examples/ip_pipeline/pipeline/pipeline_routing.h
/usr/share/dpdk/examples/ip_pipeline/pipeline/pipeline_routing_be.c
/usr/share/dpdk/examples/ip_pipeline/pipeline/pipeline_routing_be.h
/usr/share/dpdk/examples/ip_pipeline/pipeline_be.h
/usr/share/dpdk/examples/ip_pipeline/thread.c
/usr/share/dpdk/examples/ip_pipeline/thread.h
/usr/share/dpdk/examples/ip_pipeline/thread_fe.c
/usr/share/dpdk/examples/ip_pipeline/thread_fe.h
/usr/share/dpdk/examples/ip_reassembly/Makefile
/usr/share/dpdk/examples/ip_reassembly/main.c
/usr/share/dpdk/examples/ipv4_multicast/Makefile
/usr/share/dpdk/examples/ipv4_multicast/main.c
/usr/share/dpdk/examples/kni/Makefile
/usr/share/dpdk/examples/kni/main.c
/usr/share/dpdk/examples/l2fwd-crypto/Makefile
/usr/share/dpdk/examples/l2fwd-crypto/main.c
/usr/share/dpdk/examples/l2fwd-ivshmem/Makefile
/usr/share/dpdk/examples/l2fwd-ivshmem/guest/Makefile
/usr/share/dpdk/examples/l2fwd-ivshmem/guest/guest.c
/usr/share/dpdk/examples/l2fwd-ivshmem/host/Makefile
/usr/share/dpdk/examples/l2fwd-ivshmem/host/host.c
/usr/share/dpdk/examples/l2fwd-jobstats/Makefile
/usr/share/dpdk/examples/l2fwd-jobstats/main.c
/usr/share/dpdk/examples/l2fwd-keepalive/Makefile
/usr/share/dpdk/examples/l2fwd-keepalive/main.c
/usr/share/dpdk/examples/l2fwd/Makefile
/usr/share/dpdk/examples/l2fwd/main.c
/usr/share/dpdk/examples/l3fwd-acl/Makefile
/usr/share/dpdk/examples/l3fwd-acl/main.c
/usr/share/dpdk/examples/l3fwd-power/Makefile
/usr/share/dpdk/examples/l3fwd-power/main.c
/usr/share/dpdk/examples/l3fwd-vf/Makefile
/usr/share/dpdk/examples/l3fwd-vf/main.c
/usr/share/dpdk/examples/l3fwd/Makefile
/usr/share/dpdk/examples/l3fwd/main.c
/usr/share/dpdk/examples/link_status_interrupt/Makefile
/usr/share/dpdk/examples/link_status_interrupt/main.c
/usr/share/dpdk/examples/load_balancer/Makefile
/usr/share/dpdk/examples/load_balancer/config.c
/usr/share/dpdk/examples/load_balancer/init.c
/usr/share/dpdk/examples/load_balancer/main.c
/usr/share/dpdk/examples/load_balancer/main.h
/usr/share/dpdk/examples/load_balancer/runtime.c
/usr/share/dpdk/examples/multi_process/Makefile
/usr/share/dpdk/examples/multi_process/client_server_mp/Makefile
/usr/share/dpdk/examples/multi_process/client_server_mp/mp_client/Makefile
/usr/share/dpdk/examples/multi_process/client_server_mp/mp_client/client.c
/usr/share/dpdk/examples/multi_process/client_server_mp/mp_server/Makefile
/usr/share/dpdk/examples/multi_process/client_server_mp/mp_server/args.c
/usr/share/dpdk/examples/multi_process/client_server_mp/mp_server/args.h
/usr/share/dpdk/examples/multi_process/client_server_mp/mp_server/init.c
/usr/share/dpdk/examples/multi_process/client_server_mp/mp_server/init.h
/usr/share/dpdk/examples/multi_process/client_server_mp/mp_server/main.c
/usr/share/dpdk/examples/multi_process/client_server_mp/shared/common.h
/usr/share/dpdk/examples/multi_process/l2fwd_fork/Makefile
/usr/share/dpdk/examples/multi_process/l2fwd_fork/flib.c
/usr/share/dpdk/examples/multi_process/l2fwd_fork/flib.h
/usr/share/dpdk/examples/multi_process/l2fwd_fork/main.c
/usr/share/dpdk/examples/multi_process/simple_mp/Makefile
/usr/share/dpdk/examples/multi_process/simple_mp/main.c
/usr/share/dpdk/examples/multi_process/simple_mp/mp_commands.c
/usr/share/dpdk/examples/multi_process/simple_mp/mp_commands.h
/usr/share/dpdk/examples/multi_process/symmetric_mp/Makefile
/usr/share/dpdk/examples/multi_process/symmetric_mp/main.c
/usr/share/dpdk/examples/netmap_compat/Makefile
/usr/share/dpdk/examples/netmap_compat/bridge/Makefile
/usr/share/dpdk/examples/netmap_compat/bridge/bridge.c
/usr/share/dpdk/examples/netmap_compat/lib/compat_netmap.c
/usr/share/dpdk/examples/netmap_compat/lib/compat_netmap.h
/usr/share/dpdk/examples/netmap_compat/netmap/netmap.h
/usr/share/dpdk/examples/netmap_compat/netmap/netmap_user.h
/usr/share/dpdk/examples/packet_ordering/Makefile
/usr/share/dpdk/examples/packet_ordering/main.c
/usr/share/dpdk/examples/performance-thread/Makefile
/usr/share/dpdk/examples/performance-thread/common/arch/x86/ctx.c
/usr/share/dpdk/examples/performance-thread/common/arch/x86/ctx.h
/usr/share/dpdk/examples/performance-thread/common/common.mk
/usr/share/dpdk/examples/performance-thread/common/lthread.c
/usr/share/dpdk/examples/performance-thread/common/lthread.h
/usr/share/dpdk/examples/performance-thread/common/lthread_api.h
/usr/share/dpdk/examples/performance-thread/common/lthread_cond.c
/usr/share/dpdk/examples/performance-thread/common/lthread_cond.h
/usr/share/dpdk/examples/performance-thread/common/lthread_diag.c
/usr/share/dpdk/examples/performance-thread/common/lthread_diag.h
/usr/share/dpdk/examples/performance-thread/common/lthread_diag_api.h
/usr/share/dpdk/examples/performance-thread/common/lthread_int.h
/usr/share/dpdk/examples/performance-thread/common/lthread_mutex.c
/usr/share/dpdk/examples/performance-thread/common/lthread_mutex.h
/usr/share/dpdk/examples/performance-thread/common/lthread_objcache.h
/usr/share/dpdk/examples/performance-thread/common/lthread_pool.h
/usr/share/dpdk/examples/performance-thread/common/lthread_queue.h
/usr/share/dpdk/examples/performance-thread/common/lthread_sched.c
/usr/share/dpdk/examples/performance-thread/common/lthread_sched.h
/usr/share/dpdk/examples/performance-thread/common/lthread_timer.h
/usr/share/dpdk/examples/performance-thread/common/lthread_tls.c
/usr/share/dpdk/examples/performance-thread/common/lthread_tls.h
/usr/share/dpdk/examples/performance-thread/l3fwd-thread/Makefile
/usr/share/dpdk/examples/performance-thread/l3fwd-thread/main.c
/usr/share/dpdk/examples/performance-thread/l3fwd-thread/test.sh
/usr/share/dpdk/examples/performance-thread/pthread_shim/Makefile
/usr/share/dpdk/examples/performance-thread/pthread_shim/main.c
/usr/share/dpdk/examples/performance-thread/pthread_shim/pthread_shim.c
/usr/share/dpdk/examples/performance-thread/pthread_shim/pthread_shim.h
/usr/share/dpdk/examples/ptpclient/Makefile
/usr/share/dpdk/examples/ptpclient/ptpclient.c
/usr/share/dpdk/examples/qos_meter/Makefile
/usr/share/dpdk/examples/qos_meter/main.c
/usr/share/dpdk/examples/qos_meter/main.h
/usr/share/dpdk/examples/qos_meter/rte_policer.c
/usr/share/dpdk/examples/qos_meter/rte_policer.h
/usr/share/dpdk/examples/qos_sched/Makefile
/usr/share/dpdk/examples/qos_sched/app_thread.c
/usr/share/dpdk/examples/qos_sched/args.c
/usr/share/dpdk/examples/qos_sched/cfg_file.c
/usr/share/dpdk/examples/qos_sched/cfg_file.h
/usr/share/dpdk/examples/qos_sched/cmdline.c
/usr/share/dpdk/examples/qos_sched/init.c
/usr/share/dpdk/examples/qos_sched/main.c
/usr/share/dpdk/examples/qos_sched/main.h
/usr/share/dpdk/examples/qos_sched/profile.cfg
/usr/share/dpdk/examples/qos_sched/profile_ov.cfg
/usr/share/dpdk/examples/qos_sched/stats.c
/usr/share/dpdk/examples/quota_watermark/Makefile
/usr/share/dpdk/examples/quota_watermark/qw/Makefile
/usr/share/dpdk/examples/quota_watermark/qw/args.c
/usr/share/dpdk/examples/quota_watermark/qw/args.h
/usr/share/dpdk/examples/quota_watermark/qw/init.c
/usr/share/dpdk/examples/quota_watermark/qw/init.h
/usr/share/dpdk/examples/quota_watermark/qw/main.c
/usr/share/dpdk/examples/quota_watermark/qw/main.h
/usr/share/dpdk/examples/quota_watermark/qwctl/Makefile
/usr/share/dpdk/examples/quota_watermark/qwctl/commands.c
/usr/share/dpdk/examples/quota_watermark/qwctl/commands.h
/usr/share/dpdk/examples/quota_watermark/qwctl/qwctl.c
/usr/share/dpdk/examples/quota_watermark/qwctl/qwctl.h
/usr/share/dpdk/examples/rxtx_callbacks/Makefile
/usr/share/dpdk/examples/rxtx_callbacks/main.c
/usr/share/dpdk/examples/skeleton/Makefile
/usr/share/dpdk/examples/skeleton/basicfwd.c
/usr/share/dpdk/examples/tep_termination/Makefile
/usr/share/dpdk/examples/tep_termination/main.c
/usr/share/dpdk/examples/tep_termination/main.h
/usr/share/dpdk/examples/tep_termination/vxlan.c
/usr/share/dpdk/examples/tep_termination/vxlan.h
/usr/share/dpdk/examples/tep_termination/vxlan_setup.c
/usr/share/dpdk/examples/tep_termination/vxlan_setup.h
/usr/share/dpdk/examples/timer/Makefile
/usr/share/dpdk/examples/timer/main.c
/usr/share/dpdk/examples/vhost/Makefile
/usr/share/dpdk/examples/vhost/main.c
/usr/share/dpdk/examples/vhost/main.h
/usr/share/dpdk/examples/vhost_xen/Makefile
/usr/share/dpdk/examples/vhost_xen/main.c
/usr/share/dpdk/examples/vhost_xen/main.h
/usr/share/dpdk/examples/vhost_xen/vhost_monitor.c
/usr/share/dpdk/examples/vhost_xen/virtio-net.h
/usr/share/dpdk/examples/vhost_xen/xen_vhost.h
/usr/share/dpdk/examples/vhost_xen/xenstore_parse.c
/usr/share/dpdk/examples/vm_power_manager/Makefile
/usr/share/dpdk/examples/vm_power_manager/channel_manager.c
/usr/share/dpdk/examples/vm_power_manager/channel_manager.h
/usr/share/dpdk/examples/vm_power_manager/channel_monitor.c
/usr/share/dpdk/examples/vm_power_manager/channel_monitor.h
/usr/share/dpdk/examples/vm_power_manager/guest_cli/Makefile
/usr/share/dpdk/examples/vm_power_manager/guest_cli/main.c
/usr/share/dpdk/examples/vm_power_manager/guest_cli/vm_power_cli_guest.c
/usr/share/dpdk/examples/vm_power_manager/guest_cli/vm_power_cli_guest.h
/usr/share/dpdk/examples/vm_power_manager/main.c
/usr/share/dpdk/examples/vm_power_manager/power_manager.c
/usr/share/dpdk/examples/vm_power_manager/power_manager.h
/usr/share/dpdk/examples/vm_power_manager/vm_power_cli.c
/usr/share/dpdk/examples/vm_power_manager/vm_power_cli.h
/usr/share/dpdk/examples/vmdq/Makefile
/usr/share/dpdk/examples/vmdq/main.c
/usr/share/dpdk/examples/vmdq_dcb/Makefile
/usr/share/dpdk/examples/vmdq_dcb/main.c
/usr/share/dpdk/mk/arch/arm/rte.vars.mk
/usr/share/dpdk/mk/arch/arm64/rte.vars.mk
/usr/share/dpdk/mk/arch/i686/rte.vars.mk
/usr/share/dpdk/mk/arch/ppc_64/rte.vars.mk
/usr/share/dpdk/mk/arch/tile/rte.vars.mk
/usr/share/dpdk/mk/arch/x86_64/rte.vars.mk
/usr/share/dpdk/mk/arch/x86_x32/rte.vars.mk
/usr/share/dpdk/mk/exec-env/bsdapp/rte.app.mk
/usr/share/dpdk/mk/exec-env/bsdapp/rte.vars.mk
/usr/share/dpdk/mk/exec-env/linuxapp/rte.app.mk
/usr/share/dpdk/mk/exec-env/linuxapp/rte.vars.mk
/usr/share/dpdk/mk/internal/rte.build-post.mk
/usr/share/dpdk/mk/internal/rte.build-pre.mk
/usr/share/dpdk/mk/internal/rte.clean-post.mk
/usr/share/dpdk/mk/internal/rte.clean-pre.mk
/usr/share/dpdk/mk/internal/rte.compile-post.mk
/usr/share/dpdk/mk/internal/rte.compile-pre.mk
/usr/share/dpdk/mk/internal/rte.depdirs-post.mk
/usr/share/dpdk/mk/internal/rte.depdirs-pre.mk
/usr/share/dpdk/mk/internal/rte.extvars.mk
/usr/share/dpdk/mk/internal/rte.install-post.mk
/usr/share/dpdk/mk/internal/rte.install-pre.mk
/usr/share/dpdk/mk/machine/armv7-a/rte.vars.mk
/usr/share/dpdk/mk/machine/armv8a/rte.vars.mk
/usr/share/dpdk/mk/machine/atm/rte.vars.mk
/usr/share/dpdk/mk/machine/default/rte.vars.mk
/usr/share/dpdk/mk/machine/hsw/rte.vars.mk
/usr/share/dpdk/mk/machine/ivb/rte.vars.mk
/usr/share/dpdk/mk/machine/native/rte.vars.mk
/usr/share/dpdk/mk/machine/nhm/rte.vars.mk
/usr/share/dpdk/mk/machine/power8/rte.vars.mk
/usr/share/dpdk/mk/machine/snb/rte.vars.mk
/usr/share/dpdk/mk/machine/thunderx/rte.vars.mk
/usr/share/dpdk/mk/machine/tilegx/rte.vars.mk
/usr/share/dpdk/mk/machine/wsm/rte.vars.mk
/usr/share/dpdk/mk/machine/xgene1/rte.vars.mk
/usr/share/dpdk/mk/rte.app.mk
/usr/share/dpdk/mk/rte.bsdmodule.mk
/usr/share/dpdk/mk/rte.cpuflags.mk
/usr/share/dpdk/mk/rte.extapp.mk
/usr/share/dpdk/mk/rte.extlib.mk
/usr/share/dpdk/mk/rte.extobj.mk
/usr/share/dpdk/mk/rte.extshared.mk
/usr/share/dpdk/mk/rte.extsubdir.mk
/usr/share/dpdk/mk/rte.gnuconfigure.mk
/usr/share/dpdk/mk/rte.hostapp.mk
/usr/share/dpdk/mk/rte.hostlib.mk
/usr/share/dpdk/mk/rte.install.mk
/usr/share/dpdk/mk/rte.lib.mk
/usr/share/dpdk/mk/rte.module.mk
/usr/share/dpdk/mk/rte.obj.mk
/usr/share/dpdk/mk/rte.sdkbuild.mk
/usr/share/dpdk/mk/rte.sdkconfig.mk
/usr/share/dpdk/mk/rte.sdkdepdirs.mk
/usr/share/dpdk/mk/rte.sdkdoc.mk
/usr/share/dpdk/mk/rte.sdkexamples.mk
/usr/share/dpdk/mk/rte.sdkgcov.mk
/usr/share/dpdk/mk/rte.sdkinstall.mk
/usr/share/dpdk/mk/rte.sdkroot.mk
/usr/share/dpdk/mk/rte.sdktest.mk
/usr/share/dpdk/mk/rte.shared.mk
/usr/share/dpdk/mk/rte.sharelib.mk
/usr/share/dpdk/mk/rte.subdir.mk
/usr/share/dpdk/mk/rte.vars.mk
/usr/share/dpdk/mk/target/generic/rte.app.mk
/usr/share/dpdk/mk/target/generic/rte.vars.mk
/usr/share/dpdk/mk/toolchain/clang/rte.toolchain-compat.mk
/usr/share/dpdk/mk/toolchain/clang/rte.vars.mk
/usr/share/dpdk/mk/toolchain/gcc/rte.toolchain-compat.mk
/usr/share/dpdk/mk/toolchain/gcc/rte.vars.mk
/usr/share/dpdk/mk/toolchain/icc/rte.toolchain-compat.mk
/usr/share/dpdk/mk/toolchain/icc/rte.vars.mk
/usr/share/dpdk/scripts/auto-config-h.sh
/usr/share/dpdk/scripts/check-maintainers.sh
/usr/share/dpdk/scripts/checkpatches.sh
/usr/share/dpdk/scripts/cocci.sh
/usr/share/dpdk/scripts/cocci/mtod-offset.cocci
/usr/share/dpdk/scripts/depdirs-rule.sh
/usr/share/dpdk/scripts/gen-build-mk.sh
/usr/share/dpdk/scripts/gen-config-h.sh
/usr/share/dpdk/scripts/load-devel-config.sh
/usr/share/dpdk/scripts/merge-maps.sh
/usr/share/dpdk/scripts/relpath.sh
/usr/share/dpdk/scripts/test-build.sh
/usr/share/dpdk/scripts/test-null.sh
/usr/share/dpdk/scripts/validate-abi.sh
/usr/share/dpdk/tools/cpu_layout.py
/usr/share/dpdk/tools/cpu_layout.pyc
/usr/share/dpdk/tools/cpu_layout.pyo
/usr/share/dpdk/tools/dpdk_nic_bind.py
/usr/share/dpdk/tools/dpdk_nic_bind.pyc
/usr/share/dpdk/tools/dpdk_nic_bind.pyo
/usr/share/dpdk/tools/setup.sh
/usr/share/dpdk/x86_64-native-linuxapp-gcc/.config
/usr/share/dpdk/x86_64-native-linuxapp-gcc/include
/usr/share/dpdk/x86_64-native-linuxapp-gcc/lib

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/exec-env/rte_dom0_common.h
/usr/include/exec-env/rte_interrupts.h
/usr/include/exec-env/rte_kni_common.h
/usr/include/generic/rte_atomic.h
/usr/include/generic/rte_byteorder.h
/usr/include/generic/rte_cpuflags.h
/usr/include/generic/rte_cycles.h
/usr/include/generic/rte_memcpy.h
/usr/include/generic/rte_prefetch.h
/usr/include/generic/rte_rwlock.h
/usr/include/generic/rte_spinlock.h
/usr/lib64/*.so
/usr/share/dpdk/examples/l2fwd-ivshmem/include/common.h
/usr/share/dpdk/examples/quota_watermark/include/conf.h

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
