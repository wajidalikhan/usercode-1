sampleDataSet = '/QCD_Pt-120to150_MuPt5Enriched_TuneZ2_7TeV-pythia6/Summer11-PU_S4_START42_V11-v1/AODSIM'
sampleCMSEnergy = 7000

sampleRelease = "CMSSW_4_2_3_patch3" # original (i.e. RECO file) release, not the one we plan to process them with
sampleProcessRelease = "CMSSW_4_2_7" # release used to create new files with

sampleNumEvents = 8013763

sampleXSec = 92950.0 * 0.04866 # cross-section times filter efficiency

# global tag can be extracted from file using edmProvDump filename|grep globaltag
# note however that this is the tag for *further* processing, not the original tag
sampleGlobalTag = 'START42_V13::All'
sampleHLTProcess = '*'

sampleBaseDir = "root://xrootd.rcac.purdue.edu//store/user/demattia/longlived/"+sampleProcessRelease+"/QCDmu120"

sampleRecoFiles = [ ]

samplePatFiles = [
  sampleBaseDir+"/pat/PATtuple_1_1_EIz.root",
  sampleBaseDir+"/pat/PATtuple_2_1_1rH.root",
  sampleBaseDir+"/pat/PATtuple_3_1_3ND.root",
  sampleBaseDir+"/pat/PATtuple_4_1_1OI.root",
  sampleBaseDir+"/pat/PATtuple_5_1_h85.root",
  sampleBaseDir+"/pat/PATtuple_6_1_dwi.root",
  sampleBaseDir+"/pat/PATtuple_7_1_DMv.root",
  sampleBaseDir+"/pat/PATtuple_8_1_QWS.root",
  sampleBaseDir+"/pat/PATtuple_9_1_lb0.root",
  sampleBaseDir+"/pat/PATtuple_10_1_uZL.root",
  sampleBaseDir+"/pat/PATtuple_11_1_LRY.root",
  sampleBaseDir+"/pat/PATtuple_12_1_Ypp.root",
  sampleBaseDir+"/pat/PATtuple_13_1_8KN.root",
  sampleBaseDir+"/pat/PATtuple_14_1_pip.root",
  sampleBaseDir+"/pat/PATtuple_15_1_kdy.root",
  sampleBaseDir+"/pat/PATtuple_16_2_6c6.root",
  sampleBaseDir+"/pat/PATtuple_17_1_EFd.root",
  sampleBaseDir+"/pat/PATtuple_18_1_Vre.root",
  sampleBaseDir+"/pat/PATtuple_19_1_M2y.root",
  sampleBaseDir+"/pat/PATtuple_20_1_OiF.root",
  sampleBaseDir+"/pat/PATtuple_21_1_yBY.root",
  sampleBaseDir+"/pat/PATtuple_22_1_ybv.root",
  sampleBaseDir+"/pat/PATtuple_23_1_0xR.root",
  sampleBaseDir+"/pat/PATtuple_24_1_xZT.root",
  sampleBaseDir+"/pat/PATtuple_25_1_Hve.root",
  sampleBaseDir+"/pat/PATtuple_26_1_tmy.root",
  sampleBaseDir+"/pat/PATtuple_27_1_Ohr.root",
  sampleBaseDir+"/pat/PATtuple_28_1_CCW.root",
  sampleBaseDir+"/pat/PATtuple_29_1_6dP.root",
  sampleBaseDir+"/pat/PATtuple_30_1_AIu.root",
  sampleBaseDir+"/pat/PATtuple_31_1_POt.root",
  sampleBaseDir+"/pat/PATtuple_32_1_RwF.root",
  sampleBaseDir+"/pat/PATtuple_33_1_KX7.root",
  sampleBaseDir+"/pat/PATtuple_34_1_pFb.root",
  sampleBaseDir+"/pat/PATtuple_35_1_dGf.root",
  sampleBaseDir+"/pat/PATtuple_36_1_CN9.root",
  sampleBaseDir+"/pat/PATtuple_37_1_3fk.root",
  sampleBaseDir+"/pat/PATtuple_38_1_x95.root",
  sampleBaseDir+"/pat/PATtuple_39_1_FVQ.root",
  sampleBaseDir+"/pat/PATtuple_40_1_UNR.root",
  sampleBaseDir+"/pat/PATtuple_41_2_Lhx.root",
  sampleBaseDir+"/pat/PATtuple_42_2_QJQ.root",
  sampleBaseDir+"/pat/PATtuple_43_1_ihX.root",
  sampleBaseDir+"/pat/PATtuple_44_1_Ml6.root",
  sampleBaseDir+"/pat/PATtuple_45_1_nv6.root",
  sampleBaseDir+"/pat/PATtuple_46_1_A4E.root",
  sampleBaseDir+"/pat/PATtuple_47_1_NMQ.root",
  sampleBaseDir+"/pat/PATtuple_48_1_UvS.root",
  sampleBaseDir+"/pat/PATtuple_49_1_a3p.root",
  sampleBaseDir+"/pat/PATtuple_50_1_IZs.root",
  sampleBaseDir+"/pat/PATtuple_51_1_jcr.root",
  sampleBaseDir+"/pat/PATtuple_52_1_me2.root",
  sampleBaseDir+"/pat/PATtuple_53_1_JnL.root",
  sampleBaseDir+"/pat/PATtuple_54_1_QXi.root",
  sampleBaseDir+"/pat/PATtuple_55_1_KoV.root",
  sampleBaseDir+"/pat/PATtuple_56_1_su5.root",
  sampleBaseDir+"/pat/PATtuple_57_1_QWh.root",
  sampleBaseDir+"/pat/PATtuple_58_1_TjS.root",
  sampleBaseDir+"/pat/PATtuple_59_1_YRg.root",
  sampleBaseDir+"/pat/PATtuple_60_1_Rlb.root",
  sampleBaseDir+"/pat/PATtuple_61_1_A23.root",
  sampleBaseDir+"/pat/PATtuple_62_1_GDg.root",
  sampleBaseDir+"/pat/PATtuple_63_1_YjA.root",
  sampleBaseDir+"/pat/PATtuple_64_1_5DV.root",
  sampleBaseDir+"/pat/PATtuple_65_1_Hwr.root",
  sampleBaseDir+"/pat/PATtuple_66_1_LJb.root",
  sampleBaseDir+"/pat/PATtuple_67_1_q5m.root",
  sampleBaseDir+"/pat/PATtuple_68_1_viF.root",
  sampleBaseDir+"/pat/PATtuple_69_1_FGQ.root",
  sampleBaseDir+"/pat/PATtuple_70_1_Sr4.root",
  sampleBaseDir+"/pat/PATtuple_71_1_Lnz.root",
  sampleBaseDir+"/pat/PATtuple_72_1_tBR.root",
  sampleBaseDir+"/pat/PATtuple_73_1_XZh.root",
  sampleBaseDir+"/pat/PATtuple_74_1_2EW.root",
  sampleBaseDir+"/pat/PATtuple_75_1_BHd.root",
  sampleBaseDir+"/pat/PATtuple_76_1_vV2.root",
  sampleBaseDir+"/pat/PATtuple_77_1_RYj.root",
  sampleBaseDir+"/pat/PATtuple_78_1_tvZ.root",
  sampleBaseDir+"/pat/PATtuple_79_0_D0R.root",
  sampleBaseDir+"/pat/PATtuple_80_0_ZF4.root",
  sampleBaseDir+"/pat/PATtuple_81_0_E01.root",
  sampleBaseDir+"/pat/PATtuple_82_0_B6B.root",
  sampleBaseDir+"/pat/PATtuple_83_0_82l.root",
  sampleBaseDir+"/pat/PATtuple_84_0_Kwt.root",
  sampleBaseDir+"/pat/PATtuple_85_0_eOg.root",
  sampleBaseDir+"/pat/PATtuple_86_0_wQV.root",
  sampleBaseDir+"/pat/PATtuple_87_0_pbX.root",
  sampleBaseDir+"/pat/PATtuple_88_0_Ttc.root",
  sampleBaseDir+"/pat/PATtuple_89_0_0yx.root",
  sampleBaseDir+"/pat/PATtuple_90_0_s7c.root",
  sampleBaseDir+"/pat/PATtuple_91_0_O9H.root",
  sampleBaseDir+"/pat/PATtuple_92_0_Eno.root",
  sampleBaseDir+"/pat/PATtuple_93_0_mG0.root",
  sampleBaseDir+"/pat/PATtuple_94_0_XPp.root",
  sampleBaseDir+"/pat/PATtuple_95_0_YFv.root",
  sampleBaseDir+"/pat/PATtuple_96_0_ZV2.root",
  sampleBaseDir+"/pat/PATtuple_97_0_483.root",
  sampleBaseDir+"/pat/PATtuple_98_0_3M3.root",
  sampleBaseDir+"/pat/PATtuple_99_0_wUa.root",
  sampleBaseDir+"/pat/PATtuple_100_0_qqu.root",
  sampleBaseDir+"/pat/PATtuple_101_0_Vux.root",
  sampleBaseDir+"/pat/PATtuple_102_0_UxT.root",
  sampleBaseDir+"/pat/PATtuple_103_0_uCJ.root",
  sampleBaseDir+"/pat/PATtuple_104_0_djV.root",
  sampleBaseDir+"/pat/PATtuple_105_0_IRa.root",
  sampleBaseDir+"/pat/PATtuple_106_0_SWn.root",
  sampleBaseDir+"/pat/PATtuple_107_0_v6Y.root",
  sampleBaseDir+"/pat/PATtuple_108_0_Ygy.root",
  sampleBaseDir+"/pat/PATtuple_109_0_KHU.root",
  sampleBaseDir+"/pat/PATtuple_110_0_2lo.root",
  sampleBaseDir+"/pat/PATtuple_111_0_6F0.root",
  sampleBaseDir+"/pat/PATtuple_112_0_QiP.root",
  sampleBaseDir+"/pat/PATtuple_113_0_tXE.root",
  sampleBaseDir+"/pat/PATtuple_114_0_11K.root",
  sampleBaseDir+"/pat/PATtuple_115_0_UcC.root",
  sampleBaseDir+"/pat/PATtuple_116_0_yto.root",
  sampleBaseDir+"/pat/PATtuple_117_0_Bp7.root",
  sampleBaseDir+"/pat/PATtuple_118_0_GAX.root",
  sampleBaseDir+"/pat/PATtuple_119_0_3Ag.root",
  sampleBaseDir+"/pat/PATtuple_120_0_Qfh.root",
  sampleBaseDir+"/pat/PATtuple_121_0_JWZ.root",
  sampleBaseDir+"/pat/PATtuple_122_0_3nV.root",
  sampleBaseDir+"/pat/PATtuple_123_0_CHQ.root",
  sampleBaseDir+"/pat/PATtuple_124_0_Z1N.root",
  sampleBaseDir+"/pat/PATtuple_125_0_85D.root",
  sampleBaseDir+"/pat/PATtuple_126_0_PXG.root",
  sampleBaseDir+"/pat/PATtuple_127_0_8fa.root",
  sampleBaseDir+"/pat/PATtuple_128_0_Yar.root",
  sampleBaseDir+"/pat/PATtuple_129_0_GMa.root",
  sampleBaseDir+"/pat/PATtuple_130_0_dt9.root",
  sampleBaseDir+"/pat/PATtuple_131_0_gsy.root",
  sampleBaseDir+"/pat/PATtuple_132_0_CEo.root",
  sampleBaseDir+"/pat/PATtuple_133_0_C0P.root",
  sampleBaseDir+"/pat/PATtuple_134_0_QU4.root",
  sampleBaseDir+"/pat/PATtuple_135_0_lFi.root",
  sampleBaseDir+"/pat/PATtuple_136_0_xnK.root",
  sampleBaseDir+"/pat/PATtuple_137_0_y8f.root",
  sampleBaseDir+"/pat/PATtuple_138_0_PZ9.root",
  sampleBaseDir+"/pat/PATtuple_139_0_6XA.root",
  sampleBaseDir+"/pat/PATtuple_140_0_aq2.root",
  sampleBaseDir+"/pat/PATtuple_141_0_Cff.root",
  sampleBaseDir+"/pat/PATtuple_142_0_qeA.root",
  sampleBaseDir+"/pat/PATtuple_143_0_0Zx.root",
  sampleBaseDir+"/pat/PATtuple_144_0_4Ha.root",
  sampleBaseDir+"/pat/PATtuple_145_0_IdR.root",
  sampleBaseDir+"/pat/PATtuple_146_0_FQW.root",
  sampleBaseDir+"/pat/PATtuple_147_0_IPT.root",
  sampleBaseDir+"/pat/PATtuple_148_0_Eel.root",
  sampleBaseDir+"/pat/PATtuple_149_0_w6d.root",
  sampleBaseDir+"/pat/PATtuple_150_0_rHD.root",
  sampleBaseDir+"/pat/PATtuple_151_0_Jn3.root",
  sampleBaseDir+"/pat/PATtuple_152_0_TbG.root",
  sampleBaseDir+"/pat/PATtuple_153_0_94y.root",
  sampleBaseDir+"/pat/PATtuple_154_0_bKV.root",
  sampleBaseDir+"/pat/PATtuple_155_0_Ouu.root",
  sampleBaseDir+"/pat/PATtuple_156_0_d27.root",
  sampleBaseDir+"/pat/PATtuple_157_0_bFk.root",
  sampleBaseDir+"/pat/PATtuple_158_0_888.root",
  sampleBaseDir+"/pat/PATtuple_159_0_H67.root",
  sampleBaseDir+"/pat/PATtuple_160_0_IZd.root",
  sampleBaseDir+"/pat/PATtuple_161_0_kPH.root",
  sampleBaseDir+"/pat/PATtuple_162_0_1tF.root",
  sampleBaseDir+"/pat/PATtuple_163_0_eGs.root",
  sampleBaseDir+"/pat/PATtuple_164_0_Phv.root",
  sampleBaseDir+"/pat/PATtuple_165_0_TST.root",
  sampleBaseDir+"/pat/PATtuple_166_0_5Zt.root",
  sampleBaseDir+"/pat/PATtuple_167_0_yKr.root",
  sampleBaseDir+"/pat/PATtuple_168_0_NT6.root",
  sampleBaseDir+"/pat/PATtuple_169_0_PLO.root",
  sampleBaseDir+"/pat/PATtuple_170_0_6Ji.root",
  sampleBaseDir+"/pat/PATtuple_171_0_DoC.root",
  sampleBaseDir+"/pat/PATtuple_172_0_icD.root",
  sampleBaseDir+"/pat/PATtuple_173_0_VKi.root",
  sampleBaseDir+"/pat/PATtuple_174_0_zFP.root",
  sampleBaseDir+"/pat/PATtuple_175_0_VMu.root",
  sampleBaseDir+"/pat/PATtuple_176_0_wGI.root",
  sampleBaseDir+"/pat/PATtuple_177_0_ZR0.root",
  sampleBaseDir+"/pat/PATtuple_178_0_ILG.root",
  sampleBaseDir+"/pat/PATtuple_179_0_HDl.root",
  sampleBaseDir+"/pat/PATtuple_180_0_ZNp.root",
  sampleBaseDir+"/pat/PATtuple_181_0_RwJ.root",
  sampleBaseDir+"/pat/PATtuple_182_0_8fL.root",
  sampleBaseDir+"/pat/PATtuple_183_0_v9F.root",
  sampleBaseDir+"/pat/PATtuple_184_0_RnD.root",
  sampleBaseDir+"/pat/PATtuple_185_0_qiC.root",
  sampleBaseDir+"/pat/PATtuple_186_0_n6y.root",
  sampleBaseDir+"/pat/PATtuple_187_0_lcj.root",
  sampleBaseDir+"/pat/PATtuple_188_0_KZV.root",
  sampleBaseDir+"/pat/PATtuple_189_0_AkD.root",
  sampleBaseDir+"/pat/PATtuple_190_0_Adv.root",
  sampleBaseDir+"/pat/PATtuple_191_0_CSv.root",
  sampleBaseDir+"/pat/PATtuple_192_0_Vkv.root",
  sampleBaseDir+"/pat/PATtuple_193_0_3aF.root",
  sampleBaseDir+"/pat/PATtuple_194_0_rQA.root",
  sampleBaseDir+"/pat/PATtuple_195_0_u7h.root",
  sampleBaseDir+"/pat/PATtuple_196_0_3iy.root",
  sampleBaseDir+"/pat/PATtuple_197_0_cYL.root",
  sampleBaseDir+"/pat/PATtuple_198_0_SGw.root",
  sampleBaseDir+"/pat/PATtuple_199_0_PLb.root",
  sampleBaseDir+"/pat/PATtuple_200_0_I5H.root",
  sampleBaseDir+"/pat/PATtuple_201_0_FV4.root",
  sampleBaseDir+"/pat/PATtuple_202_0_P5X.root",
  sampleBaseDir+"/pat/PATtuple_203_0_aWl.root",
  sampleBaseDir+"/pat/PATtuple_204_0_wM6.root",
  sampleBaseDir+"/pat/PATtuple_205_0_17Y.root",
  sampleBaseDir+"/pat/PATtuple_206_0_zzR.root",
  sampleBaseDir+"/pat/PATtuple_207_0_FNM.root",
  sampleBaseDir+"/pat/PATtuple_208_0_hvG.root",
  sampleBaseDir+"/pat/PATtuple_209_0_hBE.root",
  sampleBaseDir+"/pat/PATtuple_210_0_MC2.root",
  sampleBaseDir+"/pat/PATtuple_211_0_BEr.root",
  sampleBaseDir+"/pat/PATtuple_212_0_hC0.root",
  sampleBaseDir+"/pat/PATtuple_213_0_iZu.root",
  sampleBaseDir+"/pat/PATtuple_214_0_B56.root",
  sampleBaseDir+"/pat/PATtuple_215_0_uSW.root",
  sampleBaseDir+"/pat/PATtuple_216_0_ol5.root",
  sampleBaseDir+"/pat/PATtuple_217_0_SX5.root",
  sampleBaseDir+"/pat/PATtuple_218_0_JhM.root",
  sampleBaseDir+"/pat/PATtuple_219_0_rUU.root",
  sampleBaseDir+"/pat/PATtuple_220_0_A8M.root",
  sampleBaseDir+"/pat/PATtuple_221_0_LWc.root",
  sampleBaseDir+"/pat/PATtuple_222_0_U6Q.root",
  sampleBaseDir+"/pat/PATtuple_223_0_TjS.root",
  sampleBaseDir+"/pat/PATtuple_224_0_uLi.root",
  sampleBaseDir+"/pat/PATtuple_225_0_WMh.root",
  sampleBaseDir+"/pat/PATtuple_226_0_b74.root",
  sampleBaseDir+"/pat/PATtuple_227_0_zmY.root",
  sampleBaseDir+"/pat/PATtuple_228_0_55h.root",
  sampleBaseDir+"/pat/PATtuple_229_0_Z5Y.root",
  sampleBaseDir+"/pat/PATtuple_230_0_E9w.root",
  sampleBaseDir+"/pat/PATtuple_231_0_NYc.root",
  sampleBaseDir+"/pat/PATtuple_232_0_H3K.root",
  sampleBaseDir+"/pat/PATtuple_233_0_KVe.root",
  sampleBaseDir+"/pat/PATtuple_234_0_ygd.root",
  sampleBaseDir+"/pat/PATtuple_235_0_CFd.root",
  sampleBaseDir+"/pat/PATtuple_236_0_TqM.root",
  sampleBaseDir+"/pat/PATtuple_237_0_JGh.root",
  sampleBaseDir+"/pat/PATtuple_238_0_FCp.root",
  sampleBaseDir+"/pat/PATtuple_239_0_UmH.root",
  sampleBaseDir+"/pat/PATtuple_240_0_R3x.root",
  sampleBaseDir+"/pat/PATtuple_241_0_XX2.root",
  sampleBaseDir+"/pat/PATtuple_242_0_hLg.root",
  sampleBaseDir+"/pat/PATtuple_243_0_WJt.root",
  sampleBaseDir+"/pat/PATtuple_244_0_qcZ.root",
  sampleBaseDir+"/pat/PATtuple_245_0_XRW.root",
  sampleBaseDir+"/pat/PATtuple_246_0_xWf.root",
  sampleBaseDir+"/pat/PATtuple_247_0_vrM.root",
  sampleBaseDir+"/pat/PATtuple_248_0_Y2x.root",
  sampleBaseDir+"/pat/PATtuple_249_0_d41.root",
  sampleBaseDir+"/pat/PATtuple_250_0_oFe.root",
  sampleBaseDir+"/pat/PATtuple_251_0_hw6.root",
  sampleBaseDir+"/pat/PATtuple_252_0_q7Q.root",
  sampleBaseDir+"/pat/PATtuple_253_0_AzB.root",
  sampleBaseDir+"/pat/PATtuple_254_0_wsJ.root",
  sampleBaseDir+"/pat/PATtuple_255_0_Syf.root",
  sampleBaseDir+"/pat/PATtuple_256_0_A4U.root",
  sampleBaseDir+"/pat/PATtuple_257_0_O5W.root",
  sampleBaseDir+"/pat/PATtuple_258_0_gXK.root",
  sampleBaseDir+"/pat/PATtuple_259_0_XzA.root",
  sampleBaseDir+"/pat/PATtuple_260_0_Xx0.root",
  sampleBaseDir+"/pat/PATtuple_261_0_89T.root",
  sampleBaseDir+"/pat/PATtuple_262_0_JWx.root",
  sampleBaseDir+"/pat/PATtuple_263_0_Wi1.root",
  sampleBaseDir+"/pat/PATtuple_264_0_4Oc.root",
  sampleBaseDir+"/pat/PATtuple_265_0_1s9.root",
  sampleBaseDir+"/pat/PATtuple_266_0_bSF.root",
  sampleBaseDir+"/pat/PATtuple_267_0_L9B.root",
  sampleBaseDir+"/pat/PATtuple_268_0_b98.root",
  sampleBaseDir+"/pat/PATtuple_269_0_ZBv.root",
  sampleBaseDir+"/pat/PATtuple_270_0_mwn.root",
  sampleBaseDir+"/pat/PATtuple_271_0_2py.root",
  sampleBaseDir+"/pat/PATtuple_272_0_HCE.root",
  sampleBaseDir+"/pat/PATtuple_273_0_eyk.root",
  sampleBaseDir+"/pat/PATtuple_274_0_ihF.root",
  sampleBaseDir+"/pat/PATtuple_275_0_Dpm.root",
  sampleBaseDir+"/pat/PATtuple_276_0_jZF.root",
  sampleBaseDir+"/pat/PATtuple_277_0_7Zm.root",
  sampleBaseDir+"/pat/PATtuple_278_0_DXL.root",
  sampleBaseDir+"/pat/PATtuple_279_0_iyd.root",
  sampleBaseDir+"/pat/PATtuple_280_0_Oun.root",
  sampleBaseDir+"/pat/PATtuple_281_0_LTU.root",
  sampleBaseDir+"/pat/PATtuple_282_0_2wi.root",
  sampleBaseDir+"/pat/PATtuple_283_0_TGD.root",
  sampleBaseDir+"/pat/PATtuple_284_0_HoG.root",
  sampleBaseDir+"/pat/PATtuple_285_0_9R2.root",
  sampleBaseDir+"/pat/PATtuple_286_0_zVD.root",
  sampleBaseDir+"/pat/PATtuple_287_0_fN8.root",
  sampleBaseDir+"/pat/PATtuple_288_0_HWf.root",
  sampleBaseDir+"/pat/PATtuple_289_0_AkI.root",
  sampleBaseDir+"/pat/PATtuple_290_0_6ek.root",
  sampleBaseDir+"/pat/PATtuple_291_0_K3B.root",
  sampleBaseDir+"/pat/PATtuple_292_0_yn9.root",
  sampleBaseDir+"/pat/PATtuple_293_0_Ivu.root",
  sampleBaseDir+"/pat/PATtuple_294_0_l98.root",
  sampleBaseDir+"/pat/PATtuple_295_0_MA1.root",
  sampleBaseDir+"/pat/PATtuple_296_0_dDw.root",
  sampleBaseDir+"/pat/PATtuple_297_0_j7k.root",
  sampleBaseDir+"/pat/PATtuple_298_0_Y7C.root",
  sampleBaseDir+"/pat/PATtuple_299_0_NSD.root",
  sampleBaseDir+"/pat/PATtuple_300_0_1ff.root",
  sampleBaseDir+"/pat/PATtuple_301_0_kJm.root",
  sampleBaseDir+"/pat/PATtuple_302_0_KN4.root",
  sampleBaseDir+"/pat/PATtuple_303_0_lUJ.root",
  sampleBaseDir+"/pat/PATtuple_304_0_rtX.root",
  sampleBaseDir+"/pat/PATtuple_305_0_gp1.root",
  sampleBaseDir+"/pat/PATtuple_306_0_c3U.root",
  sampleBaseDir+"/pat/PATtuple_307_0_YIA.root",
  sampleBaseDir+"/pat/PATtuple_308_0_aNo.root",
  sampleBaseDir+"/pat/PATtuple_309_0_JQb.root",
  sampleBaseDir+"/pat/PATtuple_310_0_R1d.root",
  sampleBaseDir+"/pat/PATtuple_311_0_X0i.root",
  sampleBaseDir+"/pat/PATtuple_312_0_nP6.root",
  sampleBaseDir+"/pat/PATtuple_313_0_Eg6.root",
  sampleBaseDir+"/pat/PATtuple_314_0_2Zy.root",
  sampleBaseDir+"/pat/PATtuple_315_0_D5B.root",
  sampleBaseDir+"/pat/PATtuple_316_0_dNz.root",
  sampleBaseDir+"/pat/PATtuple_317_0_H2j.root",
  sampleBaseDir+"/pat/PATtuple_318_0_JwY.root",
  sampleBaseDir+"/pat/PATtuple_319_0_VYM.root",
  sampleBaseDir+"/pat/PATtuple_320_0_9Ri.root",
  sampleBaseDir+"/pat/PATtuple_321_0_RZJ.root",
  sampleBaseDir+"/pat/PATtuple_322_0_OC6.root",
  sampleBaseDir+"/pat/PATtuple_323_0_2uB.root",
  sampleBaseDir+"/pat/PATtuple_324_0_BvD.root",
  sampleBaseDir+"/pat/PATtuple_325_0_wdi.root",
  sampleBaseDir+"/pat/PATtuple_326_0_7NL.root",
  sampleBaseDir+"/pat/PATtuple_327_0_FgC.root",
  sampleBaseDir+"/pat/PATtuple_328_0_jRb.root",
  sampleBaseDir+"/pat/PATtuple_329_0_Ax7.root",
  sampleBaseDir+"/pat/PATtuple_330_0_ilu.root",
  sampleBaseDir+"/pat/PATtuple_331_0_3aV.root",
  sampleBaseDir+"/pat/PATtuple_332_0_XVg.root",
  sampleBaseDir+"/pat/PATtuple_333_0_2KW.root",
  sampleBaseDir+"/pat/PATtuple_334_0_dnM.root",
  sampleBaseDir+"/pat/PATtuple_335_0_7Xy.root",
  sampleBaseDir+"/pat/PATtuple_336_0_2nt.root",
  sampleBaseDir+"/pat/PATtuple_337_0_ku1.root",
  sampleBaseDir+"/pat/PATtuple_338_0_upK.root",
  sampleBaseDir+"/pat/PATtuple_339_0_lwr.root",
  sampleBaseDir+"/pat/PATtuple_340_0_WvZ.root",
  sampleBaseDir+"/pat/PATtuple_341_0_eQG.root",
  sampleBaseDir+"/pat/PATtuple_342_0_QWq.root",
  sampleBaseDir+"/pat/PATtuple_343_0_oCI.root",
  sampleBaseDir+"/pat/PATtuple_344_0_aNM.root",
  sampleBaseDir+"/pat/PATtuple_345_0_NYa.root",
  sampleBaseDir+"/pat/PATtuple_346_0_D1p.root",
  sampleBaseDir+"/pat/PATtuple_347_0_PNS.root",
  sampleBaseDir+"/pat/PATtuple_348_0_3cf.root",
  sampleBaseDir+"/pat/PATtuple_349_0_PP2.root",
  sampleBaseDir+"/pat/PATtuple_350_0_Tra.root",
  sampleBaseDir+"/pat/PATtuple_351_0_XlQ.root",
  sampleBaseDir+"/pat/PATtuple_352_0_4io.root",
  sampleBaseDir+"/pat/PATtuple_353_0_8PQ.root",
  sampleBaseDir+"/pat/PATtuple_354_0_lj4.root",
  sampleBaseDir+"/pat/PATtuple_355_0_AOE.root",
  sampleBaseDir+"/pat/PATtuple_356_0_jJr.root",
  sampleBaseDir+"/pat/PATtuple_357_0_9Iz.root",
  sampleBaseDir+"/pat/PATtuple_358_0_AVR.root",
  sampleBaseDir+"/pat/PATtuple_359_0_dYM.root",
  sampleBaseDir+"/pat/PATtuple_360_0_2UG.root",
  sampleBaseDir+"/pat/PATtuple_361_0_TaF.root",
  sampleBaseDir+"/pat/PATtuple_362_0_sRf.root",
  sampleBaseDir+"/pat/PATtuple_363_0_l0W.root",
  sampleBaseDir+"/pat/PATtuple_364_0_VZp.root",
  sampleBaseDir+"/pat/PATtuple_365_0_rQZ.root",
  sampleBaseDir+"/pat/PATtuple_366_0_4aZ.root",
  sampleBaseDir+"/pat/PATtuple_367_0_3zy.root",
  sampleBaseDir+"/pat/PATtuple_368_0_SPP.root",
  sampleBaseDir+"/pat/PATtuple_369_0_1Ed.root",
  sampleBaseDir+"/pat/PATtuple_370_0_yOw.root",
  sampleBaseDir+"/pat/PATtuple_371_0_e6S.root",
  sampleBaseDir+"/pat/PATtuple_372_0_iMB.root",
  sampleBaseDir+"/pat/PATtuple_373_0_ut4.root",
  sampleBaseDir+"/pat/PATtuple_374_0_LCz.root",
  sampleBaseDir+"/pat/PATtuple_375_0_1YW.root",
  sampleBaseDir+"/pat/PATtuple_376_0_ckl.root",
  sampleBaseDir+"/pat/PATtuple_377_0_0uF.root",
  sampleBaseDir+"/pat/PATtuple_378_0_rWZ.root",
  sampleBaseDir+"/pat/PATtuple_379_0_c14.root",
  sampleBaseDir+"/pat/PATtuple_380_0_Z1x.root",
  sampleBaseDir+"/pat/PATtuple_381_0_6QY.root",
  sampleBaseDir+"/pat/PATtuple_382_0_G7f.root",
  sampleBaseDir+"/pat/PATtuple_383_0_Tvk.root",
  sampleBaseDir+"/pat/PATtuple_384_0_sGI.root",
  sampleBaseDir+"/pat/PATtuple_385_0_lHm.root",
  sampleBaseDir+"/pat/PATtuple_386_0_nKC.root",
  sampleBaseDir+"/pat/PATtuple_387_0_sW9.root",
  sampleBaseDir+"/pat/PATtuple_388_0_e1t.root",
  sampleBaseDir+"/pat/PATtuple_389_0_Weu.root",
  sampleBaseDir+"/pat/PATtuple_390_0_wVv.root",
  sampleBaseDir+"/pat/PATtuple_391_0_CRM.root",
  sampleBaseDir+"/pat/PATtuple_392_0_xZe.root",
  sampleBaseDir+"/pat/PATtuple_393_0_cFA.root",
  sampleBaseDir+"/pat/PATtuple_394_0_fUL.root",
  sampleBaseDir+"/pat/PATtuple_395_0_okQ.root",
  sampleBaseDir+"/pat/PATtuple_396_0_JdA.root",
  sampleBaseDir+"/pat/PATtuple_397_0_zFo.root",
  sampleBaseDir+"/pat/PATtuple_398_0_bWC.root",
  sampleBaseDir+"/pat/PATtuple_399_0_pFw.root",
  sampleBaseDir+"/pat/PATtuple_400_0_8OQ.root",
  sampleBaseDir+"/pat/PATtuple_401_0_5St.root",
  sampleBaseDir+"/pat/PATtuple_402_0_Kxc.root",
  sampleBaseDir+"/pat/PATtuple_403_0_iMg.root",
  sampleBaseDir+"/pat/PATtuple_404_0_glM.root",
  sampleBaseDir+"/pat/PATtuple_405_0_shK.root",
  sampleBaseDir+"/pat/PATtuple_406_0_Yhc.root",
  sampleBaseDir+"/pat/PATtuple_407_0_Tgk.root",
  sampleBaseDir+"/pat/PATtuple_408_0_hFe.root",
  sampleBaseDir+"/pat/PATtuple_409_0_vGE.root",
  sampleBaseDir+"/pat/PATtuple_410_0_ybh.root",
  sampleBaseDir+"/pat/PATtuple_411_0_0En.root",
  sampleBaseDir+"/pat/PATtuple_412_0_Otj.root",
  sampleBaseDir+"/pat/PATtuple_413_0_T73.root",
  sampleBaseDir+"/pat/PATtuple_414_0_40p.root",
  sampleBaseDir+"/pat/PATtuple_415_0_Kre.root",
  sampleBaseDir+"/pat/PATtuple_416_0_c1i.root",
  sampleBaseDir+"/pat/PATtuple_417_0_UfR.root",
  sampleBaseDir+"/pat/PATtuple_418_0_6rX.root",
  sampleBaseDir+"/pat/PATtuple_419_0_9Vh.root",
  sampleBaseDir+"/pat/PATtuple_420_0_tMp.root",
  sampleBaseDir+"/pat/PATtuple_421_0_M8e.root",
  sampleBaseDir+"/pat/PATtuple_422_0_nyB.root",
  sampleBaseDir+"/pat/PATtuple_423_0_tCk.root",
  sampleBaseDir+"/pat/PATtuple_424_0_XAk.root",
  sampleBaseDir+"/pat/PATtuple_425_0_Mdz.root",
  sampleBaseDir+"/pat/PATtuple_426_0_Yma.root",
  sampleBaseDir+"/pat/PATtuple_427_0_ulF.root",
  sampleBaseDir+"/pat/PATtuple_428_0_Ykm.root",
  sampleBaseDir+"/pat/PATtuple_429_0_tLg.root",
  sampleBaseDir+"/pat/PATtuple_430_0_oOP.root",
  sampleBaseDir+"/pat/PATtuple_431_0_5Q9.root",
  sampleBaseDir+"/pat/PATtuple_432_1_YHe.root",
  sampleBaseDir+"/pat/PATtuple_433_0_n6i.root",
  sampleBaseDir+"/pat/PATtuple_434_0_jPW.root",
  sampleBaseDir+"/pat/PATtuple_435_0_2WV.root",
  sampleBaseDir+"/pat/PATtuple_436_0_NMX.root",
  sampleBaseDir+"/pat/PATtuple_437_1_ERE.root",
  sampleBaseDir+"/pat/PATtuple_438_0_sWU.root",
  sampleBaseDir+"/pat/PATtuple_439_0_EzF.root",
  sampleBaseDir+"/pat/PATtuple_440_0_SWb.root",
  sampleBaseDir+"/pat/PATtuple_441_0_g5o.root",
  sampleBaseDir+"/pat/PATtuple_442_0_90e.root",
  sampleBaseDir+"/pat/PATtuple_443_0_0LI.root",
  sampleBaseDir+"/pat/PATtuple_444_0_Qhw.root",
  sampleBaseDir+"/pat/PATtuple_445_0_pvk.root",
  sampleBaseDir+"/pat/PATtuple_446_0_VFP.root",
  sampleBaseDir+"/pat/PATtuple_447_0_vpM.root",
  sampleBaseDir+"/pat/PATtuple_448_0_KLY.root",
  sampleBaseDir+"/pat/PATtuple_449_0_ZAz.root",
  sampleBaseDir+"/pat/PATtuple_450_0_yVn.root",
  sampleBaseDir+"/pat/PATtuple_451_0_LMQ.root",
  sampleBaseDir+"/pat/PATtuple_452_0_9Vr.root",
  sampleBaseDir+"/pat/PATtuple_453_0_DOs.root",
  sampleBaseDir+"/pat/PATtuple_454_0_RWF.root",
  sampleBaseDir+"/pat/PATtuple_455_0_6wf.root",
  sampleBaseDir+"/pat/PATtuple_456_0_Mq0.root",
  sampleBaseDir+"/pat/PATtuple_457_0_WId.root",
  sampleBaseDir+"/pat/PATtuple_458_0_mBG.root",
  sampleBaseDir+"/pat/PATtuple_459_0_z1g.root",
  sampleBaseDir+"/pat/PATtuple_460_0_DIH.root",
  sampleBaseDir+"/pat/PATtuple_461_0_R2q.root",
  sampleBaseDir+"/pat/PATtuple_462_0_iCP.root",
  sampleBaseDir+"/pat/PATtuple_463_0_zJO.root",
  sampleBaseDir+"/pat/PATtuple_464_0_IVS.root",
  sampleBaseDir+"/pat/PATtuple_465_0_6Ap.root",
  sampleBaseDir+"/pat/PATtuple_466_0_rlK.root",
  sampleBaseDir+"/pat/PATtuple_467_0_fjD.root",
  sampleBaseDir+"/pat/PATtuple_468_0_F14.root",
  sampleBaseDir+"/pat/PATtuple_469_0_DK3.root",
  sampleBaseDir+"/pat/PATtuple_470_0_9ck.root",
  sampleBaseDir+"/pat/PATtuple_471_0_C2b.root",
  sampleBaseDir+"/pat/PATtuple_472_0_DjX.root",
  sampleBaseDir+"/pat/PATtuple_473_0_Dk4.root",
  sampleBaseDir+"/pat/PATtuple_474_0_DMx.root",
  sampleBaseDir+"/pat/PATtuple_475_0_Y9E.root",
  sampleBaseDir+"/pat/PATtuple_476_0_9Qf.root",
  sampleBaseDir+"/pat/PATtuple_477_0_j21.root",
  sampleBaseDir+"/pat/PATtuple_478_0_Vi5.root",
  sampleBaseDir+"/pat/PATtuple_479_0_0V4.root",
  sampleBaseDir+"/pat/PATtuple_480_0_kDs.root",
  sampleBaseDir+"/pat/PATtuple_481_0_rs4.root",
  sampleBaseDir+"/pat/PATtuple_482_0_dPx.root",
  sampleBaseDir+"/pat/PATtuple_483_0_4q9.root",
  sampleBaseDir+"/pat/PATtuple_484_0_lja.root",
  sampleBaseDir+"/pat/PATtuple_485_0_OlQ.root",
  sampleBaseDir+"/pat/PATtuple_486_0_0rl.root",
  sampleBaseDir+"/pat/PATtuple_487_0_3G1.root",
  sampleBaseDir+"/pat/PATtuple_488_0_VFj.root",
  sampleBaseDir+"/pat/PATtuple_489_0_fsL.root",
  sampleBaseDir+"/pat/PATtuple_490_0_DTr.root",
  sampleBaseDir+"/pat/PATtuple_491_0_Wkc.root",
  sampleBaseDir+"/pat/PATtuple_492_0_OrS.root",
  sampleBaseDir+"/pat/PATtuple_493_0_W57.root",
  sampleBaseDir+"/pat/PATtuple_494_0_HXC.root",
  sampleBaseDir+"/pat/PATtuple_495_0_hP7.root",
  sampleBaseDir+"/pat/PATtuple_496_0_x3G.root",
  sampleBaseDir+"/pat/PATtuple_497_0_Icp.root",
  sampleBaseDir+"/pat/PATtuple_498_0_Tf2.root",
  sampleBaseDir+"/pat/PATtuple_499_0_sut.root",
  sampleBaseDir+"/pat/PATtuple_500_0_Gh0.root",
  sampleBaseDir+"/pat/PATtuple_501_0_Eka.root",
  sampleBaseDir+"/pat/PATtuple_502_0_kJg.root",
  sampleBaseDir+"/pat/PATtuple_503_0_n1A.root",
  sampleBaseDir+"/pat/PATtuple_504_0_5lw.root",
  sampleBaseDir+"/pat/PATtuple_505_0_0Yg.root",
  sampleBaseDir+"/pat/PATtuple_506_0_28u.root",
  sampleBaseDir+"/pat/PATtuple_507_0_Fud.root",
  sampleBaseDir+"/pat/PATtuple_508_0_0SS.root",
  sampleBaseDir+"/pat/PATtuple_509_0_QDe.root",
  sampleBaseDir+"/pat/PATtuple_510_0_4PD.root",
  sampleBaseDir+"/pat/PATtuple_511_0_fAN.root",
  sampleBaseDir+"/pat/PATtuple_512_0_Cgr.root",
  sampleBaseDir+"/pat/PATtuple_513_0_iqZ.root",
  sampleBaseDir+"/pat/PATtuple_514_0_eOa.root",
  sampleBaseDir+"/pat/PATtuple_515_0_uZu.root",
  sampleBaseDir+"/pat/PATtuple_516_0_K2x.root",
  sampleBaseDir+"/pat/PATtuple_517_0_sNC.root",
  sampleBaseDir+"/pat/PATtuple_518_0_nQW.root",
  sampleBaseDir+"/pat/PATtuple_519_0_CL5.root",
  sampleBaseDir+"/pat/PATtuple_520_0_GBb.root",
  sampleBaseDir+"/pat/PATtuple_521_0_eUk.root",
  sampleBaseDir+"/pat/PATtuple_522_0_HAe.root",
  sampleBaseDir+"/pat/PATtuple_523_0_1VC.root",
  sampleBaseDir+"/pat/PATtuple_524_0_1f3.root",
  sampleBaseDir+"/pat/PATtuple_525_0_cJ1.root",
  sampleBaseDir+"/pat/PATtuple_526_0_Gmy.root",
  sampleBaseDir+"/pat/PATtuple_527_0_kT4.root",
  sampleBaseDir+"/pat/PATtuple_528_0_8rp.root",
  sampleBaseDir+"/pat/PATtuple_529_0_AIW.root",
  sampleBaseDir+"/pat/PATtuple_530_0_lR6.root",
  sampleBaseDir+"/pat/PATtuple_531_0_eaz.root",
  sampleBaseDir+"/pat/PATtuple_532_0_39i.root",
  sampleBaseDir+"/pat/PATtuple_533_0_Qhw.root",
  sampleBaseDir+"/pat/PATtuple_534_0_k6X.root",
  sampleBaseDir+"/pat/PATtuple_535_0_xe5.root",
  sampleBaseDir+"/pat/PATtuple_536_0_mu9.root",
  sampleBaseDir+"/pat/PATtuple_537_0_Efj.root",
  sampleBaseDir+"/pat/PATtuple_538_0_5l8.root",
  sampleBaseDir+"/pat/PATtuple_539_0_5mj.root",
  sampleBaseDir+"/pat/PATtuple_540_0_diJ.root",
  sampleBaseDir+"/pat/PATtuple_541_0_N4J.root",
  sampleBaseDir+"/pat/PATtuple_542_0_wSA.root",
  sampleBaseDir+"/pat/PATtuple_543_0_hWv.root",
  sampleBaseDir+"/pat/PATtuple_544_0_0pn.root",
  sampleBaseDir+"/pat/PATtuple_545_0_NG7.root",
  sampleBaseDir+"/pat/PATtuple_546_0_5qH.root",
  sampleBaseDir+"/pat/PATtuple_547_0_AXd.root",
  sampleBaseDir+"/pat/PATtuple_548_0_lzB.root",
  sampleBaseDir+"/pat/PATtuple_549_0_rhz.root",
  sampleBaseDir+"/pat/PATtuple_550_0_4vS.root",
  sampleBaseDir+"/pat/PATtuple_551_0_Mmw.root",
  sampleBaseDir+"/pat/PATtuple_552_0_rMM.root",
  sampleBaseDir+"/pat/PATtuple_553_0_h3s.root",
  sampleBaseDir+"/pat/PATtuple_554_0_iIb.root",
  sampleBaseDir+"/pat/PATtuple_555_0_tci.root",
  sampleBaseDir+"/pat/PATtuple_556_0_CgW.root",
  sampleBaseDir+"/pat/PATtuple_557_0_s77.root",
  sampleBaseDir+"/pat/PATtuple_558_0_7w7.root",
  sampleBaseDir+"/pat/PATtuple_559_0_ZBT.root",
  sampleBaseDir+"/pat/PATtuple_560_0_Ftu.root",
  sampleBaseDir+"/pat/PATtuple_561_0_ElW.root",
  sampleBaseDir+"/pat/PATtuple_562_0_LZm.root",
  sampleBaseDir+"/pat/PATtuple_563_0_Zfv.root",
  sampleBaseDir+"/pat/PATtuple_564_0_f5a.root",
  sampleBaseDir+"/pat/PATtuple_565_0_0zb.root",
  sampleBaseDir+"/pat/PATtuple_566_0_7uL.root",
  sampleBaseDir+"/pat/PATtuple_567_0_rm9.root",
  sampleBaseDir+"/pat/PATtuple_568_0_Xyi.root",
  sampleBaseDir+"/pat/PATtuple_569_0_brw.root",
  sampleBaseDir+"/pat/PATtuple_570_0_JYF.root",
  sampleBaseDir+"/pat/PATtuple_571_0_PJ5.root",
  sampleBaseDir+"/pat/PATtuple_572_0_fvz.root",
  sampleBaseDir+"/pat/PATtuple_573_0_UbS.root",
  sampleBaseDir+"/pat/PATtuple_574_0_IGG.root",
  sampleBaseDir+"/pat/PATtuple_575_0_9Qw.root",
  sampleBaseDir+"/pat/PATtuple_576_0_znL.root",
  sampleBaseDir+"/pat/PATtuple_577_0_stz.root",
  sampleBaseDir+"/pat/PATtuple_578_0_uDv.root",
  sampleBaseDir+"/pat/PATtuple_579_0_oms.root",
  sampleBaseDir+"/pat/PATtuple_580_0_4RP.root",
  sampleBaseDir+"/pat/PATtuple_581_0_npr.root",
  sampleBaseDir+"/pat/PATtuple_582_0_KQT.root",
  sampleBaseDir+"/pat/PATtuple_583_0_Ocl.root",
  sampleBaseDir+"/pat/PATtuple_584_0_pNT.root",
  sampleBaseDir+"/pat/PATtuple_585_0_30W.root",
  sampleBaseDir+"/pat/PATtuple_586_0_JCD.root",
  sampleBaseDir+"/pat/PATtuple_587_0_GIE.root",
  sampleBaseDir+"/pat/PATtuple_588_0_uxf.root",
  sampleBaseDir+"/pat/PATtuple_589_0_3j2.root",
  sampleBaseDir+"/pat/PATtuple_590_0_lKO.root",
  sampleBaseDir+"/pat/PATtuple_591_0_yiI.root",
  sampleBaseDir+"/pat/PATtuple_592_0_lJQ.root",
  sampleBaseDir+"/pat/PATtuple_593_0_6Vs.root",
  sampleBaseDir+"/pat/PATtuple_594_0_yqL.root",
  sampleBaseDir+"/pat/PATtuple_595_0_8oF.root",
  sampleBaseDir+"/pat/PATtuple_596_0_qEI.root",
  sampleBaseDir+"/pat/PATtuple_597_0_Wc6.root",
  sampleBaseDir+"/pat/PATtuple_598_0_UJo.root",
  sampleBaseDir+"/pat/PATtuple_599_0_nos.root",
  sampleBaseDir+"/pat/PATtuple_600_0_ib7.root",
  sampleBaseDir+"/pat/PATtuple_601_0_zhR.root",
  sampleBaseDir+"/pat/PATtuple_602_0_44q.root",
  sampleBaseDir+"/pat/PATtuple_603_0_SyY.root",
  sampleBaseDir+"/pat/PATtuple_604_0_347.root",
  sampleBaseDir+"/pat/PATtuple_605_0_WOG.root",
  sampleBaseDir+"/pat/PATtuple_606_0_Roh.root",
  sampleBaseDir+"/pat/PATtuple_607_0_wjN.root",
  sampleBaseDir+"/pat/PATtuple_608_0_FQV.root",
  sampleBaseDir+"/pat/PATtuple_609_0_jSn.root",
  sampleBaseDir+"/pat/PATtuple_610_0_28f.root",
  sampleBaseDir+"/pat/PATtuple_611_0_OkP.root",
  sampleBaseDir+"/pat/PATtuple_612_0_vRS.root",
  sampleBaseDir+"/pat/PATtuple_613_0_Jkq.root",
  sampleBaseDir+"/pat/PATtuple_614_0_kqj.root",
  sampleBaseDir+"/pat/PATtuple_615_0_n1H.root",
  sampleBaseDir+"/pat/PATtuple_616_0_6QQ.root",
  sampleBaseDir+"/pat/PATtuple_617_0_DBp.root",
  sampleBaseDir+"/pat/PATtuple_618_0_uqr.root",
  sampleBaseDir+"/pat/PATtuple_619_0_GpY.root",
  sampleBaseDir+"/pat/PATtuple_620_0_rfc.root",
  sampleBaseDir+"/pat/PATtuple_621_0_x3s.root",
  sampleBaseDir+"/pat/PATtuple_622_0_nud.root",
  sampleBaseDir+"/pat/PATtuple_623_0_qAg.root",
  sampleBaseDir+"/pat/PATtuple_624_0_QAl.root",
  sampleBaseDir+"/pat/PATtuple_625_0_h22.root",
  sampleBaseDir+"/pat/PATtuple_626_0_SPy.root",
  sampleBaseDir+"/pat/PATtuple_627_0_Gg9.root",
  sampleBaseDir+"/pat/PATtuple_628_0_sVO.root",
  sampleBaseDir+"/pat/PATtuple_629_0_QBs.root",
  sampleBaseDir+"/pat/PATtuple_630_0_Kyq.root",
  sampleBaseDir+"/pat/PATtuple_631_0_zdI.root",
  sampleBaseDir+"/pat/PATtuple_632_0_knP.root",
  sampleBaseDir+"/pat/PATtuple_633_0_AEP.root",
  sampleBaseDir+"/pat/PATtuple_634_0_cvi.root",
  sampleBaseDir+"/pat/PATtuple_635_0_hAR.root",
  sampleBaseDir+"/pat/PATtuple_636_0_xOS.root",
  sampleBaseDir+"/pat/PATtuple_637_0_Kag.root",
  sampleBaseDir+"/pat/PATtuple_638_0_hpO.root",
  sampleBaseDir+"/pat/PATtuple_639_0_ahN.root",
  sampleBaseDir+"/pat/PATtuple_640_0_hVT.root",
  sampleBaseDir+"/pat/PATtuple_641_0_pKZ.root",
  sampleBaseDir+"/pat/PATtuple_642_1_Vwg.root",
  sampleBaseDir+"/pat/PATtuple_643_1_SGa.root",
  sampleBaseDir+"/pat/PATtuple_644_1_edU.root",
  sampleBaseDir+"/pat/PATtuple_645_1_DVS.root",
  sampleBaseDir+"/pat/PATtuple_646_1_Gi6.root",
  sampleBaseDir+"/pat/PATtuple_647_1_1Gn.root",
  sampleBaseDir+"/pat/PATtuple_648_1_rgA.root",
  sampleBaseDir+"/pat/PATtuple_649_1_3n7.root",
  sampleBaseDir+"/pat/PATtuple_650_1_3Gq.root",
  sampleBaseDir+"/pat/PATtuple_651_1_Go1.root",
  sampleBaseDir+"/pat/PATtuple_652_1_dnu.root",
  sampleBaseDir+"/pat/PATtuple_653_1_46S.root",
  sampleBaseDir+"/pat/PATtuple_654_1_vFK.root",
  sampleBaseDir+"/pat/PATtuple_655_1_Dcw.root",
  sampleBaseDir+"/pat/PATtuple_656_1_6cQ.root",
  sampleBaseDir+"/pat/PATtuple_657_1_zkJ.root",
  sampleBaseDir+"/pat/PATtuple_658_1_5tO.root",
  sampleBaseDir+"/pat/PATtuple_659_1_x1s.root",
  sampleBaseDir+"/pat/PATtuple_660_1_boH.root",
  sampleBaseDir+"/pat/PATtuple_661_1_8JK.root",
  sampleBaseDir+"/pat/PATtuple_662_1_o3r.root",
  sampleBaseDir+"/pat/PATtuple_663_1_4QG.root",
  sampleBaseDir+"/pat/PATtuple_664_1_XbB.root",
  sampleBaseDir+"/pat/PATtuple_665_1_wO4.root",
  sampleBaseDir+"/pat/PATtuple_666_1_o8g.root",
  sampleBaseDir+"/pat/PATtuple_667_1_S6o.root",
  sampleBaseDir+"/pat/PATtuple_668_1_8fq.root",
  sampleBaseDir+"/pat/PATtuple_669_1_4FM.root",
  sampleBaseDir+"/pat/PATtuple_670_1_MRN.root",
  sampleBaseDir+"/pat/PATtuple_671_1_5bI.root",
  sampleBaseDir+"/pat/PATtuple_672_1_ENt.root",
  sampleBaseDir+"/pat/PATtuple_673_1_ORh.root",
  sampleBaseDir+"/pat/PATtuple_674_1_mvQ.root",
  sampleBaseDir+"/pat/PATtuple_675_1_cEw.root",
  sampleBaseDir+"/pat/PATtuple_676_1_daS.root",
  sampleBaseDir+"/pat/PATtuple_677_1_BHo.root",
  sampleBaseDir+"/pat/PATtuple_678_1_JrU.root",
  sampleBaseDir+"/pat/PATtuple_679_1_cgB.root",
  sampleBaseDir+"/pat/PATtuple_680_1_aI4.root",
  sampleBaseDir+"/pat/PATtuple_681_1_IpZ.root",
  sampleBaseDir+"/pat/PATtuple_682_1_tqD.root",
  sampleBaseDir+"/pat/PATtuple_683_1_wN6.root",
  sampleBaseDir+"/pat/PATtuple_684_1_Q3L.root",
  sampleBaseDir+"/pat/PATtuple_685_1_DM6.root",
  sampleBaseDir+"/pat/PATtuple_686_1_8Xc.root",
  sampleBaseDir+"/pat/PATtuple_687_1_CQK.root",
  sampleBaseDir+"/pat/PATtuple_688_1_rfx.root",
  sampleBaseDir+"/pat/PATtuple_689_1_9qC.root",
  sampleBaseDir+"/pat/PATtuple_690_1_cOr.root",
  sampleBaseDir+"/pat/PATtuple_691_1_xg8.root",
  sampleBaseDir+"/pat/PATtuple_692_1_NxI.root",
  sampleBaseDir+"/pat/PATtuple_693_1_7wy.root",
  sampleBaseDir+"/pat/PATtuple_694_1_NnY.root",
  sampleBaseDir+"/pat/PATtuple_695_1_HvF.root",
  sampleBaseDir+"/pat/PATtuple_696_1_Zh3.root",
  sampleBaseDir+"/pat/PATtuple_697_1_p4z.root",
  sampleBaseDir+"/pat/PATtuple_698_1_4mS.root",
  sampleBaseDir+"/pat/PATtuple_699_1_Jsg.root",
  sampleBaseDir+"/pat/PATtuple_700_1_raU.root",
  sampleBaseDir+"/pat/PATtuple_701_1_eqS.root",
  sampleBaseDir+"/pat/PATtuple_702_1_QDC.root",
  sampleBaseDir+"/pat/PATtuple_703_1_o0B.root",
  sampleBaseDir+"/pat/PATtuple_704_1_NDx.root",
  sampleBaseDir+"/pat/PATtuple_705_1_CB6.root",
  sampleBaseDir+"/pat/PATtuple_706_1_4AI.root",
  sampleBaseDir+"/pat/PATtuple_707_1_pbt.root",
  sampleBaseDir+"/pat/PATtuple_708_1_tMm.root",
  sampleBaseDir+"/pat/PATtuple_709_1_3wF.root",
  sampleBaseDir+"/pat/PATtuple_710_1_LN9.root",
  sampleBaseDir+"/pat/PATtuple_711_1_CVF.root",
  sampleBaseDir+"/pat/PATtuple_712_1_ZUP.root",
  sampleBaseDir+"/pat/PATtuple_713_1_V5T.root",
  sampleBaseDir+"/pat/PATtuple_714_1_RTb.root",
  sampleBaseDir+"/pat/PATtuple_715_1_TZG.root",
  sampleBaseDir+"/pat/PATtuple_716_1_GPz.root",
  sampleBaseDir+"/pat/PATtuple_717_1_Iy6.root",
  sampleBaseDir+"/pat/PATtuple_718_1_NKg.root",
  sampleBaseDir+"/pat/PATtuple_719_1_tlf.root",
  sampleBaseDir+"/pat/PATtuple_720_1_Byr.root",
  sampleBaseDir+"/pat/PATtuple_721_1_syM.root",
  sampleBaseDir+"/pat/PATtuple_722_1_qZi.root",
  sampleBaseDir+"/pat/PATtuple_723_1_d7l.root",
  sampleBaseDir+"/pat/PATtuple_724_1_Q8P.root",
  sampleBaseDir+"/pat/PATtuple_725_1_etC.root",
  sampleBaseDir+"/pat/PATtuple_726_1_v4o.root",
  sampleBaseDir+"/pat/PATtuple_727_1_qWd.root",
  sampleBaseDir+"/pat/PATtuple_728_1_ja1.root",
  sampleBaseDir+"/pat/PATtuple_729_1_kG7.root",
  sampleBaseDir+"/pat/PATtuple_730_1_SSf.root",
  sampleBaseDir+"/pat/PATtuple_731_1_Y2J.root",
  sampleBaseDir+"/pat/PATtuple_732_1_uac.root",
  sampleBaseDir+"/pat/PATtuple_733_1_EYX.root",
  sampleBaseDir+"/pat/PATtuple_734_1_3kK.root",
  sampleBaseDir+"/pat/PATtuple_735_1_hmI.root",
  sampleBaseDir+"/pat/PATtuple_736_1_5LB.root",
  sampleBaseDir+"/pat/PATtuple_737_1_gaU.root",
  sampleBaseDir+"/pat/PATtuple_738_1_fOu.root",
  sampleBaseDir+"/pat/PATtuple_739_1_i5t.root",
  sampleBaseDir+"/pat/PATtuple_740_1_nyr.root",
  sampleBaseDir+"/pat/PATtuple_741_1_cLe.root",
  sampleBaseDir+"/pat/PATtuple_742_1_4cw.root",
  sampleBaseDir+"/pat/PATtuple_743_1_ZNO.root",
  sampleBaseDir+"/pat/PATtuple_744_1_liu.root",
  sampleBaseDir+"/pat/PATtuple_745_1_g6i.root",
  sampleBaseDir+"/pat/PATtuple_746_1_oul.root",
  sampleBaseDir+"/pat/PATtuple_747_1_vNA.root",
  sampleBaseDir+"/pat/PATtuple_748_1_Z72.root",
  sampleBaseDir+"/pat/PATtuple_749_1_Bo8.root",
  sampleBaseDir+"/pat/PATtuple_750_1_wfC.root",
  sampleBaseDir+"/pat/PATtuple_751_1_ajc.root",
  sampleBaseDir+"/pat/PATtuple_752_1_PJ7.root",
  sampleBaseDir+"/pat/PATtuple_753_1_v7E.root",
  sampleBaseDir+"/pat/PATtuple_754_1_29D.root",
  sampleBaseDir+"/pat/PATtuple_755_1_Csy.root",
  sampleBaseDir+"/pat/PATtuple_756_1_Szd.root",
  sampleBaseDir+"/pat/PATtuple_757_1_Zvt.root",
  sampleBaseDir+"/pat/PATtuple_758_1_ZEZ.root",
  sampleBaseDir+"/pat/PATtuple_759_1_3Vf.root",
  sampleBaseDir+"/pat/PATtuple_760_1_iRt.root",
  sampleBaseDir+"/pat/PATtuple_761_1_g03.root",
  sampleBaseDir+"/pat/PATtuple_762_1_rsz.root",
  sampleBaseDir+"/pat/PATtuple_763_1_GOe.root",
  sampleBaseDir+"/pat/PATtuple_764_1_XnT.root",
  sampleBaseDir+"/pat/PATtuple_765_1_8VV.root",
  sampleBaseDir+"/pat/PATtuple_766_1_Q2w.root",
  sampleBaseDir+"/pat/PATtuple_767_1_OiP.root",
  sampleBaseDir+"/pat/PATtuple_768_1_kIh.root",
  sampleBaseDir+"/pat/PATtuple_769_1_BsB.root",
  sampleBaseDir+"/pat/PATtuple_770_1_7jo.root",
  sampleBaseDir+"/pat/PATtuple_771_1_P19.root",
  sampleBaseDir+"/pat/PATtuple_772_1_YIK.root",
  sampleBaseDir+"/pat/PATtuple_773_1_hyI.root",
  sampleBaseDir+"/pat/PATtuple_774_1_DBG.root",
  sampleBaseDir+"/pat/PATtuple_775_1_9hs.root",
  sampleBaseDir+"/pat/PATtuple_776_1_SHs.root",
  sampleBaseDir+"/pat/PATtuple_777_1_DJ9.root",
  sampleBaseDir+"/pat/PATtuple_778_1_kff.root",
  sampleBaseDir+"/pat/PATtuple_779_1_TBV.root",
  sampleBaseDir+"/pat/PATtuple_780_1_OVu.root",
  sampleBaseDir+"/pat/PATtuple_781_1_LsJ.root",
  sampleBaseDir+"/pat/PATtuple_782_1_eer.root",
  sampleBaseDir+"/pat/PATtuple_783_1_Cvn.root",
  sampleBaseDir+"/pat/PATtuple_784_1_AiM.root",
  sampleBaseDir+"/pat/PATtuple_785_1_0G5.root",
  sampleBaseDir+"/pat/PATtuple_786_1_Rdm.root",
  sampleBaseDir+"/pat/PATtuple_787_1_rSV.root",
  sampleBaseDir+"/pat/PATtuple_788_1_rpB.root",
  sampleBaseDir+"/pat/PATtuple_789_1_XK4.root",
  sampleBaseDir+"/pat/PATtuple_790_1_XFw.root",
  sampleBaseDir+"/pat/PATtuple_791_1_i1E.root",
  sampleBaseDir+"/pat/PATtuple_792_1_Bxh.root",
  sampleBaseDir+"/pat/PATtuple_793_1_UoI.root",
  sampleBaseDir+"/pat/PATtuple_794_1_68f.root",
  sampleBaseDir+"/pat/PATtuple_795_1_J9I.root",
  sampleBaseDir+"/pat/PATtuple_796_1_KAT.root",
  sampleBaseDir+"/pat/PATtuple_797_1_0L5.root",
  sampleBaseDir+"/pat/PATtuple_798_1_Xfp.root",
  sampleBaseDir+"/pat/PATtuple_799_1_1ST.root",
  sampleBaseDir+"/pat/PATtuple_800_1_GQC.root",
  sampleBaseDir+"/pat/PATtuple_801_1_PwX.root",
  sampleBaseDir+"/pat/PATtuple_802_1_0vZ.root",
  sampleBaseDir+"/pat/PATtuple_803_1_LvH.root"
]

sampleDuplicateCheckMode = 'checkAllFilesOpened'

sampleType = "MC"
sampleRunE = 0