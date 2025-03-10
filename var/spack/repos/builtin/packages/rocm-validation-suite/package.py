# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class RocmValidationSuite(CMakePackage):
    """The ROCm Validation Suite (RVS) is a system administrators
    and cluster manager's tool for detecting and troubleshooting
    common problems affecting AMD GPU(s) running in a high-performance
    computing environment, enabled using the ROCm software stack on a
    compatible platform."""

    homepage = "https://github.com/ROCm-Developer-Tools/ROCmValidationSuite"
    url = "https://github.com/ROCm-Developer-Tools/ROCmValidationSuite/archive/rocm-5.2.3.tar.gz"
    tags = ["rocm"]

    maintainers = ["srekolam", "renjithravindrankannath"]

    version("5.2.3", sha256="5dfbd41c694bf2eb4368edad8653dc60ec2927d174fc7aaa5fa416156c5f921f")
    version("5.2.1", sha256="a0ea3ab9cbb8ac17bfa4537713a4d7075f869949bfdead4565a46f75864bd4a9")
    version("5.2.0", sha256="2dfef5d66f544230957ac9aaf647b2f1dccf3cc7592cc322cae9fbdcf3321365")
    version("5.1.3", sha256="0140a4128c31749c078d9e1dc863cbbd690efc65843c34a4b80f0056e5b8c7b6")
    version("5.1.0", sha256="d9b9771b885bd94e5d0352290d3fe0fa12f94ce3f384c3844002cd7614880010")
    version("5.0.2", sha256="f249fe700a5a96c6dabf12130a3e366ae6025fe1442a5d11d08801d6c0265af4")
    version("5.0.0", sha256="d4ad31db0377096117714c9f4648cb37d6808ce618cd0bb5e4cc89cc9b4e37fd")
    version("4.5.2", sha256="e2a128395367a60a17d4d0f62daee7d34358c75332ed582243b18da409589ab8")
    version("4.5.0", sha256="54181dd5a132a7f4a34a9316d8c00d78343ec45c069c586134ce4e61e68747f5")
    version(
        "4.3.1",
        sha256="779a3b0afb53277e41cf863185e87f95d9b2bbb748fcb062cbb428d0b510fb69",
        deprecated=True,
    )
    version(
        "4.3.0",
        sha256="f7a918b513c51dd5eadce3f2e091679b2dfe6544a913960ac483567792a06a4c",
        deprecated=True,
    )
    version(
        "4.2.0",
        sha256="b25e58a842a8eb90bfd6c4ae426ca5cfdd5de2f8a091761f83597f7cfc2cd0f3",
        deprecated=True,
    )
    version(
        "4.1.0",
        sha256="f9618f89384daa0ae897b36638a3737bcfa47e98778e360338267cd1fe2bbc66",
        deprecated=True,
    )
    version(
        "4.0.0",
        sha256="04743ca8901b94a801759a3c13c8caf3e6ea950ffcda6408173e6f9ef7b86e74",
        deprecated=True,
    )
    version(
        "3.10.0",
        sha256="9f9a530f7850770663e0b0ec0c786367f2e22500a472ac6652c4fd9fb4df4f64",
        deprecated=True,
    )
    version(
        "3.9.0",
        sha256="17662028a4485b97e3ccaad5e94d20aaa2c3e9e3f741c7ebbf0f8b4cdebcc555",
        deprecated=True,
    )
    version(
        "3.8.0",
        sha256="68f1c5102e5cbed205a0ecf5a01efbdccf480f7e484ab1e58cbc6bc03e428122",
        deprecated=True,
    )
    version(
        "3.7.0",
        sha256="bb42d7fb7ee877b80ce53b0cd1f04b0c8301197b6777d2edddcb44732bf8c9e2",
        deprecated=True,
    )
    version(
        "3.5.0",
        sha256="273e67ecce7e32939341679362b649f3361a36a22fab5f64cefe94b49e6f1e46",
        deprecated=True,
    )

    variant(
        "build_type",
        default="Release",
        values=("Release", "Debug", "RelWithDebInfo"),
        description="CMake build type",
    )

    patch("001-fixes-for-rocblas-rocm-smi-install-prefix-path.patch", when="@4.1.0:4.3.2")
    patch("002-remove-force-setting-hip-inc-path.patch", when="@4.1.0:4.3.2")
    patch("003-cmake-change-to-remove-installs-and-sudo.patch", when="@4.1.0:4.3.2")
    patch("004-remove-git-download-yaml-cpp-use-yaml-cpp-recipe.patch", when="@4.3.0:4.3.2")
    patch("005-cleanup-path-reference-donot-download-googletest-yaml.patch", when="@4.5.0:")
    patch("006-library-path.patch", when="@4.5.0:")

    depends_on("cmake@3.5:", type="build")
    depends_on("zlib", type="link")
    depends_on("yaml-cpp~shared")
    depends_on("googletest~shared", when="@4.5.0:")
    depends_on("doxygen", type="build", when="@4.5.0:")

    def setup_build_environment(self, build_env):
        spec = self.spec
        build_env.set("HIPCC_PATH", spec["hip"].prefix)

    for ver in [
        "3.5.0",
        "3.7.0",
        "3.8.0",
        "3.9.0",
        "3.10.0",
        "4.0.0",
        "4.1.0",
        "4.2.0",
        "4.3.0",
        "4.3.1",
        "4.5.0",
        "4.5.2",
        "5.0.0",
        "5.0.2",
        "5.1.0",
        "5.1.3",
        "5.2.0",
        "5.2.1",
        "5.2.3",
    ]:
        depends_on("hip@" + ver, when="@" + ver)
        depends_on("rocminfo@" + ver, when="@" + ver)
        depends_on("rocblas@" + ver, when="@" + ver)
        depends_on("rocm-smi-lib@" + ver, when="@" + ver)

    for ver in [
        "3.5.0",
        "3.7.0",
        "3.8.0",
        "3.9.0",
        "3.10.0",
        "4.0.0",
        "4.1.0",
        "4.2.0",
        "4.3.0",
        "4.3.1",
    ]:
        depends_on("hip-rocclr@" + ver, when="@" + ver)

    def patch(self):
        if "@4.5.0:5.1" in self.spec:
            filter_file(
                "@ROCM_PATH@/rvs", self.spec.prefix.rvs, "rvs/conf/deviceid.sh.in", string=True
            )
        elif "@5.2.0:" in self.spec:
            filter_file(
                "@ROCM_PATH@/bin", self.spec.prefix.bin, "rvs/conf/deviceid.sh.in", string=True
            )

    def cmake_args(self):
        args = [
            self.define("HIP_PATH", self.spec["hip"].prefix),
            self.define("HSA_PATH", self.spec["hsa-rocr-dev"].prefix),
            self.define("ROCM_SMI_DIR", self.spec["rocm-smi-lib"].prefix),
            self.define("ROCBLAS_DIR", self.spec["rocblas"].prefix),
            self.define("YAML_INC_DIR", self.spec["yaml-cpp"].prefix.include),
            self.define("YAML_LIB_DIR", self.spec["yaml-cpp"].libs.directories[0]),
        ]
        if self.spec.satisfies("@4.5.0:"):
            args.append(self.define("UT_INC", self.spec["googletest"].prefix.include))
            libloc = self.spec["googletest"].prefix.lib64
            if not os.path.isdir(libloc):
                libloc = self.spec["googletest"].prefix.lib
            args.append(self.define("UT_LIB", libloc))
            libloc = self.spec["hsakmt-roct"].prefix.lib64
            if not os.path.isdir(libloc):
                libloc = self.spec["hsakmt-roct"].prefix.lib
            args.append(self.define("HSAKMT_LIB_DIR", libloc))
        return args
