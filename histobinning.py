from args_analysis import args


binningRules = [
    (".*_pt", "30 , 0, 300"),
    ("Dijets_mass", "3000, 50, 200"),
    ("Z.*_mass", "3000, 10, 150"),
    (".*_dphi", "30, 0, 3.2"),
    (".*_deta", "30, 0, 5"),
    (".*_dr", "30, 0, 10"),
    (".*_ptRatio", "30, 0, 2"),
    ("btag.*", "30, 0, 1") if not args.btag_bin else ("btag.*", "4, -0.5, 3.5"),
    ("SoftActivityJetNjets5", "12, -0.5, 11.5"),
    ("DNN_Score", "10000, 0, 1"),
    ("atanhDNN_Score", "10000, 0, 15"),
    ("hadronFlavour_btag.*", "6, -0.5, 5.5"),
    ("LHE_Nb", "6, -0.5, 5.5"),
    ("btagWeight.*", "100, 0, 10"),
]
binningRules += [(".*_pt_.*", "30, 0, 300")]
binningRules += [
    (jer, "100, 0, 5")
    for jer in [
        "Jet_jerNomSF",
        "Jet_jerUpSF",
        "Jet_jerDownSF",
    ]
]
