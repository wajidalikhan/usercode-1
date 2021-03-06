//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Mon Mar  5 13:27:07 2012 by ROOT version 5.32/00
// from TTree T/L2Muons
// found on file: hltL2Muons.root
//////////////////////////////////////////////////////////

#ifndef AnalyzeTree_h
#define AnalyzeTree_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <vector>

// Header file for the classes stored in the TTree if any.
#include <../../RootTreeProducers/interface/Track.h>
#include <../../RootTreeProducers/interface/GenParticle.h>
#ifdef __CINT__
#pragma link off all globals;
#pragma link off all classes;
#pragma link off all functions;
#pragma link C++ class Track+;
#pragma link C++ class std::vector<Track>+;
#pragma link C++ class GenParticle+;
#pragma link C++ class std::vector<GenParticle>+;
#endif

// Fixed size dimensions of array or collections stored in the TTree if any.

class AnalyzeTree {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

   // Declaration of leaf types
   UInt_t          event;
   UInt_t          run;
   std::vector<Track>   *tracks;
   std::vector<GenParticle> *genParticles;

   // List of branches
   TBranch        *b_event;   //!
   TBranch        *b_run;   //!
   TBranch        *b_tracks;   //!
   TBranch        *b_genParticles;   //!

   AnalyzeTree(TTree *tree=0);
   virtual ~AnalyzeTree();
   virtual Int_t    Cut();//Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef AnalyzeTree_cxx
AnalyzeTree::AnalyzeTree(TTree *tree) : fChain(0) 
{
  // TFile * f = new TFile("hltL2Muons_new.root");
  // TFile * f = new TFile("hltL2Muons_old.root");
  TFile * f = new TFile("cosmicMuons1Leg.root");
  f->GetObject("T",tree);
  Init(tree);
}

AnalyzeTree::~AnalyzeTree()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t AnalyzeTree::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t AnalyzeTree::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (fChain->GetTreeNumber() != fCurrent) {
      fCurrent = fChain->GetTreeNumber();
      Notify();
   }
   return centry;
}

void AnalyzeTree::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set object pointer
   tracks = 0;
   genParticles = 0;
   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("event", &event, &b_event);
   fChain->SetBranchAddress("run", &run, &b_run);
   fChain->SetBranchAddress("tracks", &tracks, &b_tracks);
   fChain->SetBranchAddress("genParticles", &genParticles, &b_genParticles);
   Notify();
}

Bool_t AnalyzeTree::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void AnalyzeTree::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t AnalyzeTree::Cut()//Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef AnalyzeTree_cxx
