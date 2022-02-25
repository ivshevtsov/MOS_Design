import matplotlib.pyplot as plt
from Functions import read_file
import numpy as np
import skrf as rf
plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"


def Input_impedance_LNA():
    Measure = rf.Network(f'Files\LNA\LNA_Input/LNA_CL_2_4.5мА_0.95V.s1p')
    Model_TT = rf.Network(f'Files\LNA\LNA_Input/LNA_Input_PEX_TT.s2p')
    Model_FF = rf.Network(f'Files\LNA\LNA_Input/LNA_Input_PEX_FF.s2p')
    Model_SS = rf.Network(f'Files\LNA\LNA_Input/LNA_Input_PEX_SS.s2p')

    plt.figure()
    plt.title('Входной импеданс МШУ')
    Measure.plot_s_smith(m=0, n=0, label='Measure', linewidth='3')
    Model_TT.plot_s_smith(m=0, n=0, label='Model(TT)', linewidth='3')
    Model_FF.plot_s_smith(m=0, n=0, label='Model(FF)', linewidth='3')
    Model_SS.plot_s_smith(m=0, n=0, label='Model(SS)', linewidth='3')
    plt.grid()

    plt.figure()
    plt.title('Входной импеданс МШУ')
    Measure.plot_s_db(m=0, n=0, label='Measure', linewidth='3')
    Model_TT.plot_s_db(m=0, n=0, label='Model(TT)', linewidth='3')
    Model_FF.plot_s_db(m=0, n=0, label='Model(FF)', linewidth='3')
    Model_SS.plot_s_db(m=0, n=0, label='Model(SS)', linewidth='3')
    plt.ylabel('S11, дБ')
    plt.xlabel('F, Гц')
    plt.grid()

    plt.figure()
    plt.title('Входной импеданс МШУ')
    plt.plot(Measure.f, Measure.z_im[:, 0, 0], label='Measure', linewidth='3')
    plt.plot(Model_TT.f, Model_TT.z_im[:, 0, 0], label='Model(TT)', linewidth='3')
    plt.plot(Model_FF.f, Model_FF.z_im[:, 0, 0], label='Model(FF)', linewidth='3')
    plt.plot(Model_SS.f, Model_SS.z_im[:, 0, 0], label='Model(SS)', linewidth='3')
    plt.grid()
    plt.legend()
    plt.xlabel('F, Гц')
    plt.ylabel('Z11(Im), Ом')

    plt.figure()
    plt.title('Входной импеданс МШУ')
    plt.plot(Measure.f, Measure.z_re[:, 0, 0], label='Measure', linewidth='3')
    plt.plot(Model_TT.f, Model_TT.z_re[:, 0, 0], label='Model(TT)', linewidth='3')
    plt.plot(Model_FF.f, Model_FF.z_re[:, 0, 0], label='Model(FF)', linewidth='3')
    plt.plot(Model_SS.f, Model_SS.z_re[:, 0, 0], label='Model(SS)', linewidth='3')
    plt.grid()
    plt.legend()
    plt.xlabel('F, Гц')
    plt.ylabel('Z11(Re), Ом')

def One_port_prove():
    D_Measure = rf.Network(f'Files\LNA\LNA_Input/sma_in_lna.s1p')
    Calc_Measure = rf.Network(f'Files\LNA\LNA_Input/One_port_Zin(M).s1p')

    plt.figure()
    plt.title('Полосковая линия с МШУ')
    D_Measure.plot_s_smith(m=0, n=0, label='Прямое измерение', linewidth='3')
    Calc_Measure.plot_s_smith(m=0, n=0, label='Однопортовый метод', linewidth='3')
    plt.grid()

    plt.figure()
    plt.title('Полосковая линия с МШУ')
    D_Measure.plot_s_db(m=0, n=0, label='Прямое измерение', linewidth='3')
    Calc_Measure.plot_s_db(m=0, n=0, label='Однопортовый метод', linewidth='3')
    plt.ylabel('S11, дБ')
    plt.xlabel('F, Гц')
    plt.grid()

    plt.figure()
    plt.title('Полосковая линия с МШУ')
    plt.plot(D_Measure.f, D_Measure.z_im[:, 0, 0], label='Прямое измерение', linewidth='3')
    plt.plot(Calc_Measure.f, Calc_Measure.z_im[:, 0, 0], label='Однопортовый метод', linewidth='3')
    plt.grid()
    plt.legend()
    plt.xlabel('F, Гц')
    plt.ylabel('Z11(Im), Ом')

    plt.figure()
    plt.title('Полосковая линия с МШУ')
    plt.plot(D_Measure.f, D_Measure.z_re[:, 0, 0], label='Прямое измерение', linewidth='3')
    plt.plot(Calc_Measure.f, Calc_Measure.z_re[:, 0, 0], label='Однопортовый метод', linewidth='3')
    plt.grid()
    plt.legend()
    plt.xlabel('F, Гц')
    plt.ylabel('Z11(Re), Ом')

def One_port_Dut():
    Line_DUT = rf.Network(f'Files/LNA/One_port/Results/DUT_Result.s2p')

    plt.figure()
    plt.title('Полосковая линия')
    Line_DUT.plot_s_smith(m=0, n=0, label='S11', linewidth='3')
    Line_DUT.plot_s_smith(m=1, n=1, label='S22', linewidth='3')
    plt.grid()

    plt.figure()
    plt.title('Полосковая линия')
    Line_DUT.plot_s_db(m=0, n=0, label='S11', linewidth='3')
    Line_DUT.plot_s_db(m=1, n=1, label='S22', linewidth='3')
    plt.ylabel('S11, дБ')
    plt.xlabel('F, Гц')
    plt.grid()

    plt.figure()
    plt.title('Полосковая линия')
    plt.plot(Line_DUT.f, Line_DUT.z_im[:, 0, 0], label='Z11', linewidth='3')
    plt.plot(Line_DUT.f, Line_DUT.z_im[:, 1, 1], label='Z22', linewidth='3')
    plt.grid()
    plt.legend()
    plt.xlabel('F, Гц')
    plt.ylabel('Z(Im), Ом')

    plt.figure()
    plt.title('Полосковая линия')
    plt.plot(Line_DUT.f, Line_DUT.z_re[:, 0, 0], label='Z11', linewidth='3')
    plt.plot(Line_DUT.f, Line_DUT.z_re[:, 1, 1], label='Z22', linewidth='3')
    plt.grid()
    plt.legend()
    plt.xlabel('F, Гц')
    plt.ylabel('Z(Re), Ом')

Measure = rf.Network(f'Files/LNA/LNA_Input/ind_10n.s1p')
Sim = rf.Network(f'Files/LNA/LNA_Input/ind_10n_sim.s1p')

plt.figure()
Measure.plot_s_smith(m=0, n=0, label='Измерение', linewidth='3')
Sim.plot_s_smith(m=0, n=0, label='Моделирование', linewidth='3')
plt.grid()

plt.figure()
Measure.plot_s_db(m=0, n=0, label='Измерение', linewidth='3')
Sim.plot_s_db(m=0, n=0, label='Моделирование', linewidth='3')
plt.ylabel('S11, дБ')
plt.xlabel('F, Гц')
plt.grid()

plt.figure()
plt.plot(Measure.f, Measure.z_im[:, 0, 0], label='Измерение', linewidth='3')
plt.plot(Sim.f, Sim.z_im[:, 0, 0], label='Моделирование', linewidth='3')
plt.grid()
plt.legend()
plt.xlabel('F, Гц')
plt.ylabel('Z(Im), Ом')

plt.figure()
plt.plot(Measure.f, Measure.z_re[:, 0, 0], label='Измерение', linewidth='3')
plt.plot(Sim.f, Sim.z_re[:, 0, 0], label='Моделирование', linewidth='3')
plt.grid()
plt.legend()
plt.xlabel('F, Гц')
plt.ylabel('Z(Re), Ом')





plt.show()