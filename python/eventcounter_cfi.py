import FWCore.ParameterSet.Config as cms

eventCounter = cms.EDAnalyzer('EventCounter',
    genEvtInfoProdName         = cms.string('generator'),
    isData                     = cms.bool    (False),
)
