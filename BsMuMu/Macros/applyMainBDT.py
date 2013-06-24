from setdirs import *
#from mvalib import *


"""
apply Main BDT on cross-check analysis data input
"""

#rootDir="rootfiles/"

method="BDT"
Region = ""
cutValue = -999


def main():

    outputfilelist = ""
    outputfilelistB = ""
    outputfilelistE= ""

    mainBdtCut = { "barrel":0.350, "endcaps":0.368 }
    #mainBdtCut = { "barrel":0, "endcaps":0 }

    #main ana BDT application
    for isample in range(3):
        for ireg in range(2,4):
            #if isample!=0 or ireg!=2:
            #    continue
            if ireg==2:
                Region="Barrel"
                cutValue = mainBdtCut["barrel"]
            elif ireg==3:
                Region="Endcaps"
                cutValue = mainBdtCut["endcaps"]
            mainWeightFile = "weights_main/TMVA-"+str(ireg)+"-Events"+str(isample)+"_BDT.weights.xml"
            inputFile = rootDir + Region + "_preselection_"+str(isample)+".root"
            outputFile = inputFile.split(".")[0] + "_mainBDTapplied.root"
            outputfilelist += " " + outputFile
            if ireg==2:outputfilelistB += " " + outputFile
            if ireg==3:outputfilelistE += " " + outputFile

            print isample, Region, mainWeightFile, inputFile, outputFile
            os.system("root -l -b -q TMVAClassificationApplication_main.C+\(\\\""+inputFile+"\\\",\\\""+outputFile+"\\\",\\\""+mainWeightFile+"\\\","+str(cutValue)+",\\\""+method+"\\\"\)")

    #merge files
    #print "hadd rootfiles/all_mainBDTapplied.root",outputfilelist
    os.system("hadd -f "+rootDir+"all_mainBDTapplied.root"+outputfilelist)
    os.system("hadd -f "+rootDir+"barrel_mainBDTapplied.root"+outputfilelistB)
    os.system("hadd -f "+rootDir+"endcaps_mainBDTapplied.root"+outputfilelistE)


    # display plots
    for region in regions:
        TMVAPlots(region)

    exit(66)

    #display mass plot and event count after each Cnc cut
    for region in regions:
        sequential_count(region)



#list of main analysis CnC cuts
listOfCntCutsBarrel = ["",
                 "((m1pt>m2pt && m1pt>4.5 && m2pt>4.0)||(m1pt<m2pt && m1pt>4.0 && m2pt>4.5))",
                 "pt>6.5", "pvw8>0.6","pvip<0.008", "pvips<2",  
                 "alpha<0.05", "chi2dof<2.2", "fls3d>13", "iso>0.8", "maxdoca>0.015", "closetrk<2" 
                 ]
listOfCntCutsEndcaps = ["",
                       "((m1pt>m2pt && m1pt>4.5 && m2pt>4.2)||(m1pt<m2pt && m1pt>4.2 && m2pt>4.5))",
                 "pt>8.5", "pvw8>0.6","pvip<0.008", "pvips<2",  
                 "alpha<0.03", "chi2dof<1.8", "fls3d>15", "iso>0.8", "maxdoca>0.015", "closetrk<2" 
                 ]

Ncuts = len(listOfCntCutsBarrel)
    
gStyle.SetOptStat(0)

def sequential_count(region):
    Region = region[:1].upper()+region[1:] #capitalize first letter for retrieving file names
    fname = rootDir + Region+"_preselection.root"
    print fname
    inputFile = TFile(rootDir + Region+"_preselection.root")
    inputDir = inputFile.Get("probe_tree")
    cuts = ""
    icol=0
    massPlot = []
    evtcount = []

    #for icut,cut in enumerate(listOfCntCuts):
    for icut in range(Ncuts):
        if icut>1:
            cuts += " && "
        if region=="barrel":
            cuts += listOfCntCutsBarrel[icut]
        elif region == "endcaps":
            cuts += listOfCntCutsEndcaps[icut]
        else:
            exit(99)
        hname = "hn"+str(icut)
        inputDir.Draw("m>>"+hname,cuts)
        massPlot.append(TROOT.gROOT.FindObject(hname))
        icol += 1
        if icol%10==0: icol+=1
        massPlot[icut].SetLineColor(icol)
        evtcount.append(massPlot[icut].GetEntries())
        print icut,"++"+cuts+"++", hname, evtcount[icut]
    canvas = TCanvas()
    tl = TLatex()
    tl.SetNDC();
    tl.SetTextSize( 0.033 );
    step = 0.05
    yy = 0.75
    massPlot[0].SetTitle(region)
    icol=0
    for icut in range(Ncuts):
        if icut==0: massPlot[icut].Draw()
        else: massPlot[icut].Draw("same")
        yy-=step
        icol += 1
        if icol%10==0: icol+=1
        tl.SetTextColor(icol)
        txt = listOfCntCutsBarrel[icut]
        if region not in "barrel":
            txt = listOfCntCutsEndcaps[icut]
        txt=txt.split("<")[0].split(">")[0].replace("(","")+": "
        if icut==0:
            yy+=2*step
            tl.DrawLatex(0.38,yy,"preselection")
            yy-=step
        txt += str("%i" % evtcount[icut])
        tl.DrawLatex(0.38,yy,txt)
        if icut==0:
            tl.DrawLatex(0.38,yy,"")
            yy-=step

    canvas.SaveAs(plotsDir+"mass_cnt_"+region+".gif")
    canvas.SaveAs(figuresDird+"mass_cnt_"+region+".pdf")



def TMVAPlots(region):
    inputFile = TFile(rootDir+region+"_mainBDTapplied.root")
    #names = [k.GetName() for k in inputFile.GetListOfKeys()]
    #print names
    histoList = inputFile.GetListOfKeys()
    for key in histoList:
        #print key.GetName()
        histo = key.ReadObj()
        if isinstance(histo, TH1F):
            name = histo.GetName()
            #name = fullName.split("__")[0]
            #hType = fullName.split("__")[1].split("_")[0]
            canvas = TCanvas(name+"_canvas")
            #stack = THStack(name+"_stack", name)
            histo.Draw()
            histo.SetLineColor(4)
            histo.SetFillColor(4);
            histo.SetFillStyle(3004);
            #leg = TLegend(0.5536913,0.770979,0.9345638,0.9702797,"","brNDC")
            #leg.AddEntry(histo, hType, "f")
            canvas.Draw()
            canvas.SaveAs(plotsDir+name+"_"+region+".gif")
            canvas.SaveAs(figuresDird+name+"_"+region+".pdf")



if __name__=="__main__":
   main()


"""
TMVA-2-Events0_BDT.weights.xml is for type-0 events in 2012 barrel
TMVA-3-Events0_BDT.weights.xml is for type-0 events in 2013 endcap

TMVA-2-Events1_BDT.weights.xml is for type-1 events in 2012 barrel
TMVA-3-Events1_BDT.weights.xml is for type-1 events in 2013 endcap

"""
