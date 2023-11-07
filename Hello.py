# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger#olsnibibdibsdioa
#njpofijnpi

LOGGER = get_logger(__name__)
#iuhgiuh

def run():
    st.set_page_config(
        page_title="EcoGuardian",
        page_icon="🦎",
    )
st.title('Bem vindo ao :red[ECOGUARDIAN]')
st.header('Aqui com a ajuda de uma IA você pode indentificar animais exóticos fora de seu habtat', divider='blue')
st.header('Teste')
st.write("teste do teste ")

if __name__ == "__main__":
    run()
