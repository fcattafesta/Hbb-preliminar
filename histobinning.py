from btagging_sys import btag_sys

binningRules = [
    (".*_pt", "30 , 0, 300"),
    ("Dijets_mass", "30, 50, 200"),
    ("Z.*_mass", "28, 10, 150"),
    (".*_dphi", "30, 0, 3.2"),
    (".*_deta", "30, 0, 5"),
    (".*_dr", "30, 0, 10"),
    (".*_ptRatio", "30, 0, 2"),
    ("btag.*", "30, 0, 1"),
    ("SoftActivityJetNjets5", "12, -0.5, 11.5"),
    ("DNN_Score", "10000, 0, 1"),
    ("atanhDNN_Score", "10000, 0, 15"),
    ("hadronFlavour_btag.*", "6, -0.5, 5.5"),
    ("LHE_Nb", "6, -0.5, 5.5"),
    ("btagWeightCentral", "100, 0, 10"),
]
binningRules += [
    (weight, "100, 0, 10") for weight in btag_sys
]

