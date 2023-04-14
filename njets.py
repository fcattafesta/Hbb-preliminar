import ROOT


def lhe_njets(df, njets):
    df.Define("LHE_selectedNjets", f"LHE_Njets={njets}")
    return df


def njet(path, njets, outpath):
    df = ROOT.RDataFrame("Events", path)

    h_pre = df.Histo1D(("", "", 5, 0, 5), "LHE_Njets")

    df = lhe_njets(df, njets)

    h_post = df.Histo1D(("", "", 5, 0, 5), "LHE_selectedNjets")

    # plot
    ROOT.gStyle.SetOptFit(0)
    ROOT.gStyle.SetTextFont(42)
    c = ROOT.TCanvas("c", "c", 800, 700)
    c.SetLeftMargin(0.15)

    h_pre.SetTitle("")
    h_pre.GetXaxis().SetTitle("LHE_Njets")
    h_pre.GetXaxis().SetTitleSize(0.04)
    h_pre.GetYaxis().SetTitle("Normalized Events / 1 GeV")
    h_pre.GetYaxis().SetTitleSize(0.04)
    h_pre.SetFillColorAlpha(ROOT.kBlue - 3, 0.5)
    h_pre.SetLineWidth(2)
    h_pre.SetLineStyle(2)

    h_post.SetFillColorAlpha(ROOT.kOrange + 7, 0.2)
    h_post.SetLineWidth(2)

    h_pre.DrawClone("hist")
    h_post.DrawClone("hist same")

    legend = ROOT.TLegend(0.72, 0.75, 0.89, 0.88)
    legend.SetFillColor(0)
    legend.SetFillStyle(0)
    legend.SetBorderSize(0)
    legend.SetTextSize(0.02)
    legend.AddEntry(h_pre, "pre-cut", "f")
    legend.AddEntry(h_post, "post-cut", "f")
    legend.DrawClone("NDC NB")

    cms_label = ROOT.TLatex()
    cms_label.SetTextSize(0.04)
    cms_label.DrawLatexNDC(0.16, 0.92, "#bf{CMS} #it{Private Work}")
    c.Update()
    c.SaveAs(outpath)