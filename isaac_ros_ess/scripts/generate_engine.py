#!/usr/bin/env python3

# SPDX-FileCopyrightText: NVIDIA CORPORATION & AFFILIATES
# Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0

# This script generats the ESS model engine file

import argparse

from isaac_ros_ess.engine_generator import ESSEngineGenerator


def get_args():
    parser = argparse.ArgumentParser(
        description='ESS model engine generator with tao-converter')
    parser.add_argument('--etlt_model', default='', help='ESS etlt model.')
    parser.add_argument('--arch',
                        default='x86_64',
                        help='Architecture of the target platform.'
                             'Options: x86_64 and aarch64. Default is x86_64.')
    return parser.parse_args()


def main():
    args = get_args()
    gen = ESSEngineGenerator(etlt_model=args.etlt_model, arch=args.arch)
    gen.generate()


if __name__ == '__main__':
    main()
