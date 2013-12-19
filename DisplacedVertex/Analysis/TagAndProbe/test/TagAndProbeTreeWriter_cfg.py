import FWCore.ParameterSet.Config as cms

process = cms.Process("TagAndProbeTreeWriter")

# # initialize MessageLogger and output report
# process.load("FWCore.MessageLogger.MessageLogger_cfi")
# # process.MessageLogger.cerr.threshold = 'INFO'
# # process.MessageLogger.categories.append('Demo')
# # process.MessageLogger.cerr.INFO = cms.untracked.PSet(
# #     limit = cms.untracked.int32(-1)
# # )

process.load("FWCore.MessageService.test.Services_cff")
# Here is the configuration of the MessgeLogger Service:
process.MessageLogger = cms.Service("MessageLogger",
    destinations = cms.untracked.vstring('Message'),
    Message = cms.untracked.PSet(
        threshold = cms.untracked.string('INFO')
    )
)

process.load("Configuration.StandardSequences.Services_cff")
process.load('Configuration.StandardSequences.Reconstruction_cff')

process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")
# process.load('Configuration.StandardSequences.MagneticField_cff')

# Careful, this needs to be changed for the data
#This is for MC
#process.GlobalTag.globaltag = 'FT_53_V6C_AN3::All'
#This is for data
process.GlobalTag.globaltag = 'FT_53_V6C_AN3::All'

# process.load("MagneticField.Engine.uniformMagneticField_cfi")

process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source('PoolSource',
                            fileNames = cms.untracked.vstring( *(
    "/store/mc/Summer12_DR53X/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/AODSIM/PU_S10_START53_V7A-v1/0000/7CCFB834-02D2-E111-BAFE-001E67397F35.root",
    ) )
                            )

process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')

process.demo = cms.EDAnalyzer('TagAndProbeTreeWriter',
                              UseMCtruth = cms.bool(True),
                              MuonCollection = cms.InputTag("globalMuons"),
                              StandAloneMuonCollection = cms.InputTag("refittedStandAloneMuons"),
                              # Note: this collection is also used for the track-based isolation
                              TrackCollection = cms.InputTag("generalTracks"),
                              # TriggerMuonCollection = cms.InputTag("L2Muons"),
                              OutputName = cms.string("tagAndProbe_MC.root"),
                              # Give a substring of the trigger or the full name. Do not use a *.
                              TriggerNames = cms.vstring("IsoMu24_v", "HLT_L2DoubleMu23_NoVertex_2Cha_Angle2p5_v", "HLT_L2DoubleMu23_NoVertex_v"),
                              # They must correspond to the names given in the TriggerNames parameter
                              FilterNames = cms.vstring("hltL3crIsoL1sMu16L1f0L2f16QL3f24QL3crIsoRhoFiltered0p15", "hltL2DoubleMu23NoVertexL2Filtered2ChaAngle2p5", "hltL2DoubleMu23NoVertexL2PreFiltered"),
                              MinTrackPt = cms.double(15.),
                              MinMuonPt = cms.double(15.),
                              MinStandAloneMuonPt = cms.double(15)
                              )

process.p = cms.Path(process.demo)
