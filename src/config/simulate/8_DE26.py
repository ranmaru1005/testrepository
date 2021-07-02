import numpy as np

config = {
    'eta': 0.996,  # 結合損
    'alpha': 52.96,  # 伝搬損失係数
    'K': np.array([
        0.47743963743586515, 0.08279863027165452, 0.15802943464483438, 0.1054167512329105, 0.042871509025034726, 0.06281171376630318, 0.04667455134846743, 0.08889416596285005, 0.6877026248495882
    ]),  # 結合率
    'L': np.array([
        5.495454545454545e-05, 8.243181818181816e-05, 0.0002198181818181818, 5.495454545454545e-05, 8.243181818181816e-05, 8.243181818181816e-05, 5.495454545454545e-05, 8.243181818181816e-05
    ]),  # リング周長
    'n_eff': 2.2,  # 実行屈折率
    'n_g': 4.4,  # 群屈折率
    'center_wavelength': 1550e-9,
    'lambda': np.arange(1520e-9, 1560e-9, 1e-12)
}
