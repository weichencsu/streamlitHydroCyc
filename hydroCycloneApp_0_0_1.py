import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# SETTING PAGE CONFIG TO WIDE MODE
#st.set_page_config(layout="wide")
#image = Image.open('bradken.png')
#st.image(image, width = 50)


def main():
    st.set_page_config(page_title='水力旋流器选型', initial_sidebar_state = 'auto')
    #page_icon = favicon,
    st.markdown(
            f"""
            <style>
                .reportview-container .main .block-container{{
                    max-width: 1200px;
                    padding-top: 1rem;
                    padding-right: 1rem;
                    padding-left: 1rem;
                    padding-bottom: 1rem;
                }}

            </style>
            """,
            unsafe_allow_html=True,
        )

    #
    #            .reportview-container .main {{
    #                color: {COLOR};
    #                background-color: {BACKGROUND_COLOR};
    #            }}

    # sidebar settings
    st.sidebar.markdown("现有旋流器工件情况（没有不填）")
    r1 = st.sidebar.text_input('旋流器规格 - [mm]')
    r2 = st.sidebar.text_input('给矿口尺寸 - [mm]')
    r3 = st.sidebar.text_input('溢流口尺寸 - [mm]')
    r4 = st.sidebar.text_input('沉砂口尺寸 - [mm]')
    r5 = st.sidebar.text_input('锥     角 - [ᵒ]')
    r6 = st.sidebar.text_input('给矿压力 - [kPa]')
    r7 = st.sidebar.text_input('给矿浓度 - [%]')
    r8 = st.sidebar.text_input('溢流中-200目含量 - [%]')
    r9 = st.sidebar.text_input('溢流浓度 - [%]')
    r10 = st.sidebar.text_input('现旋流器存在的问题')


    # main section
    st.subheader('江西耐普矿机水力旋流器选型软件')

    projectInfo = st.expander("项目信息", True)
    with projectInfo:
        r1col1, r1col2, r1col3 = projectInfo.columns(3)
        r1col1.text_input('客户名称')
        r1col2.text_input('联 系 人')
        r1col3.text_input('电    话')
        r2col1, r2col2, r2col3 = projectInfo.columns(3)
        r2col1.text_input('Email')
        r2col2.text_input('微 信')
        r2col3.text_input('QQ')

    application = st.expander("旋流器用途", True)
    with application:
        application.radio('请选择旋流器应用场景', ["分级", "脱水", "胶泥", "除杂", "浓缩", "筑坝"])
        application.text_input('其他-请说明')
        application.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    parameters = st.expander("指标参数", True)
    with parameters:
        #parameters.container("1.旋流器给矿条件")
        parameters.write("1. 旋流器给矿条件")
        # first row
        r1col1, r1col2, r1col3 = parameters.columns(3)
        r1col1.text_input('处理矿石名称')
        oreDen = r1col2.text_input('矿 石 密 度 - [t/m³]', '0')
        feedWt = r1col3.text_input('给矿重量浓度 - [%]', '0')
        # second row
        r2col1, r2col2, r2col3 = parameters.columns(3)
        r2col1.text_input('矿浆温度 - [ᵒC]')
        dryton = r2col2.text_input('干矿处理量 - [t/h]', '0')
        rcyload = r2col3.text_input('循环负荷 - [%]', '0')
        # third row
        parameters.text_input('给矿-200目含量 - [%]')
        # seconds container
        parameters.write("2. 要求旋流器的工作效果")
        # first row
        rr1col1, rr1col2, = parameters.columns(2)
        ovfSF = rr1col1.text_input('溢流细度(-200目含量) - [%]', '0')
        ovfWt = rr1col2.text_input('溢流质量浓度 - [%]', '0')

    # 物料平衡计算
    # 分为两列
    massbalance = st.expander('物料平衡计算', True)
    with massbalance:
        massbalance.write("工作条件")
        # 显示已输入参数
        MB_r1col1, MB_r1col2, MB_r1col3 = massbalance.columns(3)
        MB_r1col1.metric(label="干矿处理量 - [t/h]", value=dryton)
        MB_r1col1.metric(label="溢流细度(-200目含量) - [%]", value=ovfSF)
        MB_r1col2.metric(label="循环负荷 - [%]", value=rcyload)
        MB_r1col2.metric(label="矿石密度 - [t/m³]", value=oreDen)
        MB_r1col3.metric(label="溢流质量浓度 - [%]", value=ovfWt)
        MB_r1col3.metric(label="给矿重量浓度 - [%]", value=feedWt)
        
        # 显示物料平衡
        massbalance.write("物料平衡")
        # 下面显示pandas dataframe. 根据用户选择的不同
        mssBcol1, mssBcol2 = massbalance.columns(2)
        with mssBcol1.form(key = "my_form1"):
            mssBcol1.text_input("沉沙质量浓度 - [%]")
            mssBcol1.text_input("细度-200目含量1 - [%]")
            submitted1 = mssBcol1.button(label = '计算物料平衡1')
        with mssBcol2.form(key = "my_form2"):
            mssBcol2.text_input("给矿质量浓度 - [%]")
            mssBcol2.text_input("细度-200目含量2 - [%]")
            submitted2 = mssBcol2.button(label = '计算物料平衡2')

        df = pd.read_excel('massBalance_1.xlsx', index_col=0)
        st.table(df)


    # 结构参数
    strucPara = st.expander("结构参数", True)
    with strucPara:
        # 台数参数
        SP_r1col1, SP_r1col2, SP_r1col3 = strucPara.columns(3)
        SP_r1col1.text_input("工件台数")
        SP_r1col2.text_input("备用台数")
        SP_r1col3.metric(label="单台需能力 - [m³/h]", value=500)
        # 工作压力
        # 计算工作压力 与 人为设置工作压力
        SPP_r1col1, SPP_r1col2, SPP_r1col3 = strucPara.columns(3)
        SPP_r1col1.metric(label="计算工作压力 - [MPa]", value=0.065)
        SPP_r1col1.latex(r''' 
            \Delta P_{m} = 10.7 \rho_{m} V_{i}^{2} \left(\frac{d_{i}}{D}\right)^{2} \lbrack\left( 1.5\frac{D}{d_{o}} \right)^{1.28}-1\rbrack
            ''')
        SPP_r1col2.metric(label="计算直径 - [cm]", value=81)
        SPP_r1col2.latex(r''' 
            D = 1.95 q_{m}^{0.5} \rho_{m}^{0.25} \Delta P_{m}^{-0.25}
            ''')
        SPP_r1col3.text_input("设置工作压力 - [MPa]")
        # 计算工作压力 与 人为设置工作压力
        SPPP_r1col1, SPPP_r1col2, SPPP_r1col3 = strucPara.columns(3)
        SPPP_r1col1.text_input("型号(直径) - [mm]")
        SPPP_r1col1.text_input("溢 流 口 - [mm]")
        SPPP_r1col1.text_input("溢流管插入深度 - [mm]")
        SPPP_r1col2.text_input("阀门直径 - [mm]")
        SPPP_r1col2.text_input("沉 砂 咀 - [mm]")
        SPPP_r1col2.text_input("锥    角 - [度]")
        SPPP_r1col3.text_input("给 矿 口 - [mm]")
        SPPP_r1col3.text_input("筒 体 高 - [mm]")

#   结构参数
    manufCap = st.expander("生产能力计算", True)
    with manufCap:
        MC_col1, MC_col2, MC_col3 = manufCap.columns(3)
        MC_col1.metric(label="计算生产能力 - [m³/h]", value=705)
        MC_col1.latex(r''' 
            q_{m} = 2.69 D d_{i} ( \, \frac{\Delta P_{m}}{\rho_{m} [ \, ( \, 1.5\frac{D}{d_{0}} ) \,^{1.28} - 1 ] \, } ) \,^{0.5}
            ''')
        MC_col2.metric(label="数量", value=11.8)
        MC_col3.text_input("人为设置数量")

#   结构参数
    sizeClss = st.expander("分级粒度校核", True)
    with sizeClss:
        SC_col1, SC_col2 = sizeClss.columns(2)
        SC_col1.metric(label="粘度 - [Pa.s]", value=0.00162)
        SC_col1.latex(r''' 
            \mu_{m} = \mu [ \, 1 + 2.5 C_{iv} + 10.05 C_{iv}^{2} + 0.00273 e^{16.6C_{iv}} ] \,
            ''')
        SC_col2.metric(label="分级粒度 - [um]", value=102.4)
        SC_col2.latex(r''' 
            d_{m} = 1815 ( \, \frac{D^{0.36}d_{0}^{0.64} d_{i} \rho_{m}^{0.5} \mu_{m}}{( \,\delta - \rho_{m}) \, ( \, 3D - 2 d_{0}) \, \Delta P_{m}^{0.5}} \tan \frac{\theta}{2} ) \,^{0.5}
            ''')
    #   结构参数
    sandsink = st.expander("校核沉砂能力", True)
    with sandsink:
        SS_col1, SS_col2, SS_col3 = sandsink.columns(3)
        SS_col1.metric(label="设计沉砂能力 - [t/h]", value=274.7)
        SS_col1.markdown("2.06 t/cm².h")
        SS_col2.metric(label="排口比", value=0.47)
        SS_col3.metric(label="分级效率 - [%]", value=60.75)



if __name__ == "__main__":
    main()


