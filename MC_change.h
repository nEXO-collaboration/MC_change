#ifndef MC_change_h
#define MC_change_h

#include "SniperKernel/AlgBase.h"
#include "TROOT.h"
#include "TFile.h"
#include "TTree.h"
#include "TH1.h"
#include "TH2.h"
#include <vector>
#include "TVector3.h"
#include "TObject.h"
#include "TBranch.h"


class MC_change: public AlgBase
{
   public:
      MC_change(const std::string& name);
      ~MC_change();

      bool initialize();
      bool execute();
      bool finalize();
//    void GetGen();


   private:
      std::string InputMCName;
      std::string InputMCDir;
      int EVENT;
      TFile *f;
      TTree *t1;
      int fEventNumber;
      double fGenX;
      double fGenY;
      double fGenZ;
      double fTotalEventEnergy;
      int fInitNOP;
      int fNTE;
      std::vector<float> *fpTEEnergy;
      std::vector<float> *fpTEX;
      std::vector<float> *fpTEY;
      std::vector<float> *fpTEZ;
      std::vector<double> fTEEnergy;
      std::vector<double> fTEX;
      std::vector<double> fTEY;
      std::vector<double> fTEZ;

};

#endif
