#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class GslMicrosoftConan(ConanFile):
    name = "gsl_microsoft"
    version = "20171020"
    commit_id = "211e195d8f9dd6fa967a5741387fb5eae1ff351b"
    description = "Functions and types that are suggested for use by the C++ Core Guideline"
    url = "https://github.com/bincrafters/conan-gsl_microsoft"
    license = "MIT"
    exports = ["LICENSE.md"]
    source_subfolder = "source_subfolder"
    
    def source(self):
        source_url = "https://github.com/Microsoft/GSL"
        tools.get("{0}/archive/{1}.zip".format(source_url, self.commit_id))
        extracted_dir = "GSL-" + self.commit_id
        os.rename(extracted_dir, self.source_subfolder)
            
    def package(self):
        include_folder = os.path.join(self.source_subfolder,"include")
        self.copy(pattern="LICENSE", src=self.source_subfolder)
        self.copy(pattern="*", dst="include", src=include_folder)

    def package_id(self):
        self.info.header_only()
