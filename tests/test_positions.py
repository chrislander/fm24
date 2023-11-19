# test_positions.py

import unittest
from fm import parse_individual_position, parse_position_string, calculate_personality_score, calculate_position_score

class TestParsePositionString(unittest.TestCase):

    def test_DM_M_C(self):
        self.assertEqual(set(parse_position_string('DM, M (C)')), {'dm', 'mc'})

    def test_D_WB_R(self):
        self.assertEqual(set(parse_position_string('D/WB (R)')), {'dr', 'wbr'})

    def test_D_LC_WB_L(self):
        self.assertEqual(set(parse_position_string('D (LC), WB (L)')), {'dl', 'dc', 'wbl'})

    def test_D_WB_L(self):
        self.assertEqual(set(parse_position_string('D/WB (L)')), {'dl', 'wbl'})

    def test_M_RC_AM_C_ST_C(self):
        self.assertEqual(set(parse_position_string('M (RC), AM (C), ST (C)')), {'mr', 'mc', 'amc', 'sc'})

    def test_D_RL_WB_AM_L(self):
        self.assertEqual(set(parse_position_string('D (RL), WB/AM (L)')), {'dr', 'dl', 'wbl', 'aml'})

    def test_GK(self):
        self.assertEqual(set(parse_position_string('GK')), {'gk'})

    def test_D_RC(self):
        self.assertEqual(set(parse_position_string('D (RC)')), {'dr', 'dc'})

    def test_D_C_DM_M_C(self):
        self.assertEqual(set(parse_position_string('D (C), DM, M (C)')), {'dc', 'dm', 'mc'})

    def test_D_C_DM_M_AM_C(self):
        self.assertEqual(set(parse_position_string('D (C), DM, M/AM (C)')), {'dc', 'dm', 'mc', 'amc'})

    def test_D_RC_WB_R(self):
        self.assertEqual(set(parse_position_string('D (RC), WB (R)')), {'dr', 'dc', 'wbr'})

    def test_D_LC_DM(self):
        self.assertEqual(set(parse_position_string('D (LC), DM')), {'dl', 'dc', 'dm'})

    def test_D_WB_RL_AM_L(self):
        self.assertEqual(set(parse_position_string('D/WB (RL), AM (L)')), {'dr', 'dl', 'wbr', 'wbl', 'aml'})

    def test_WB_M_AM_R(self):
        self.assertEqual(set(parse_position_string('WB/M/AM (R)')), {'wbr', 'mr', 'amr'})

    def test_DM_M_C_AM_RC(self):
        self.assertEqual(set(parse_position_string('DM, M (C), AM (RC)')), {'dm', 'mc', 'amr', 'amc'})

    def test_M_AM_R(self):
        self.assertEqual(set(parse_position_string('M/AM (R)')), {'mr', 'amr'})

    def test_M_AM_C(self):
        self.assertEqual(set(parse_position_string('M/AM (C)')), {'mc', 'amc'})

    def test_M_AM_RC(self):
        self.assertEqual(set(parse_position_string('M/AM (RC)')), {'mr', 'amr', 'mc', 'amc'})

    def test_M_R_AM_RL(self):
        self.assertEqual(set(parse_position_string('M (R), AM (RL)')), {'mr', 'aml', 'amr'})

    def test_M_AM_L_ST_C(self):
        self.assertEqual(set(parse_position_string('M/AM (L), ST (C)')), {'ml', 'aml', 'sc'})

    def test_M_R_AM_RL_ST_C(self):
        self.assertEqual(set(parse_position_string('M (R), AM (RL), ST (C)')), {'mr', 'aml', 'amr', 'sc'})

    def test_AM_L(self):
        self.assertEqual(set(parse_position_string('AM (L)')), {'aml'})

    def test_AM_RC_ST_C(self):
        self.assertEqual(set(parse_position_string('AM (RC), ST (C)')), {'amr', 'amc', 'sc'})

    def test_AM_C_ST_C(self):
        self.assertEqual(set(parse_position_string('AM (C), ST (C)')), {'amc', 'sc'})

    def test_ST_C(self):
        self.assertEqual(set(parse_position_string('ST (C)')), {'sc'})

    def test_AM_RLC_ST_C(self):
        self.assertEqual(set(parse_position_string('AM (RLC), ST (C)')), {'aml', 'amr', 'amc', 'sc'})

    def test_AM_RL_ST_C(self):
        self.assertEqual(set(parse_position_string('AM (RL), ST (C)')), {'aml', 'amr', 'sc'})

    def test_M_R_AM_RC_ST_C(self):
        self.assertEqual(set(parse_position_string('M (R), AM (RC), ST (C)')), {'mr', 'amr', 'amc', 'sc'})

    def test_DM_M_C(self):
        self.assertEqual(set(parse_position_string('DM, M (C)')), {'dm', 'mc'})

    def test_D_RLC(self):
        self.assertEqual(set(parse_position_string('D (RLC)')), {'dr', 'dl', 'dc'})

    def test_DM_M_C_AM_LC(self):
        self.assertEqual(set(parse_position_string('DM, M (C), AM (LC)')), {'dm', 'mc', 'aml', 'amc'})

    def test_M_AM_C_ST_C(self):
        self.assertEqual(set(parse_position_string('M/AM (C), ST (C)')), {'mc', 'amc', 'sc'})

    def test_M_R_AM_RL_ST_C(self):
        self.assertEqual(set(parse_position_string('M (R), AM (RL), ST (C)')), {'mr', 'aml', 'amr', 'sc'})

    def test_M_AM_RLC_ST_C(self):
        self.assertEqual(set(parse_position_string('M/AM (RLC), ST (C)')), {'mr', 'ml', 'mc', 'amr', 'aml', 'amc', 'sc'})

    def test_D_RC_WB_R_DM(self):
        self.assertEqual(set(parse_position_string('D (RC), WB (R), DM')), {'dr', 'dc', 'wbr', 'dm'})

    def test_M_R_AM_RLC_ST_C(self):
        self.assertEqual(set(parse_position_string('M (R), AM (RLC), ST (C)')), {'mr', 'amr', 'aml', 'amc', 'sc'})

    def test_M_L_AM_RLC(self):
        self.assertEqual(set(parse_position_string('M (L), AM (RLC)')), {'ml', 'aml', 'amr', 'amc'})

    def test_D_RL_WB_M_AM_L(self):
        self.assertEqual(set(parse_position_string('D (RL), WB/M/AM (L)')), {'dr', 'dl', 'wbl', 'ml', 'aml'})

    def test_D_C_DM(self):
        self.assertEqual(set(parse_position_string('D (C), DM')), {'dc', 'dm'})

    def test_DM_M_AM_C(self):
        self.assertEqual(set(parse_position_string('DM, M/AM (C)')), {'dm', 'mc', 'amc'})

    def test_M_RC_AM_RLC(self):
        self.assertEqual(set(parse_position_string('M (RC), AM (RLC)')), {'mr', 'mc', 'aml', 'amr', 'amc'})

    def test_D_C_WB_R_DM(self):
        self.assertEqual(set(parse_position_string('D (C), WB (R), DM')), {'dc', 'wbr', 'dm'})

    def test_D_LC_WB_L_DM(self):
        self.assertEqual(set(parse_position_string('D (LC), WB (L), DM')), {'dl', 'dc', 'wbl', 'dm'})

    def test_D_WB_M_AM_L(self):
        self.assertEqual(set(parse_position_string('D/WB/M/AM (L)')), {'dl', 'wbl', 'ml', 'aml'})

    def test_D_WB_L(self):
        self.assertEqual(set(parse_position_string('D/WB (L)')), {'dl', 'wbl'})

    def test_DM_M_C_AM_RLC_ST_C(self):
        self.assertEqual(set(parse_position_string('DM, M (C), AM (RLC), ST (C)')), {'dm', 'mc', 'aml', 'amr', 'amc', 'sc'})

    def test_AM_L_ST_C(self):
        self.assertEqual(set(parse_position_string('AM (L), ST (C)')), {'aml', 'sc'})

    def test_M_C_AM_RLC_ST_C(self):
        self.assertEqual(set(parse_position_string('M (C), AM (RLC), ST (C)')), {'mc', 'aml', 'amr', 'amc', 'sc'})

    def test_D_WB_M_L(self):
        self.assertEqual(set(parse_position_string('D/WB/M (L)')), {'dl', 'wbl', 'ml'})

    def test_M_AM_RL(self):
        self.assertEqual(set(parse_position_string('M/AM (RL)')), {'mr', 'ml', 'amr', 'aml'})

    def test_M_C_AM_RC_ST_C(self):
        self.assertEqual(set(parse_position_string('M (C), AM (RC), ST (C)')), {'mc', 'amr', 'amc', 'sc'})

    def test_D_RL_WB_R_DM_M_RLC_AM_R(self):
        self.assertEqual(set(parse_position_string('D (RL), WB (R), DM, M (RLC), AM (R)')), {'dr', 'dl', 'wbr', 'dm', 'mr', 'ml', 'mc', 'amr'})

    def test_D_R_DM(self):
        self.assertEqual(set(parse_position_string('D (R), DM')), {'dr', 'dm'})

    def test_M_LC_AM_C_ST_C(self):
        self.assertEqual(set(parse_position_string('M (LC), AM (C), ST (C)')), {'ml', 'mc', 'amc', 'sc'})

    def test_D_WB_RL_M_AM_R(self):
        self.assertEqual(set(parse_position_string('D/WB (RL), M/AM (R)')), {'dr', 'dl', 'wbr', 'wbl', 'mr', 'amr'})

    def test_D_WB_R_DM_M_R(self):
        self.assertEqual(set(parse_position_string('D/WB (R), DM, M (R)')), {'dr', 'wbr', 'dm', 'mr'})

    def test_D_LC_M_L(self):
        self.assertEqual(set(parse_position_string('D (LC), M (L)')), {'dl', 'dc', 'ml'})

    def test_WB_R_DM(self):
        self.assertEqual(set(parse_position_string('WB (R), DM')), {'wbr', 'dm'})

    def test_WB_R_M_RC(self):
        self.assertEqual(set(parse_position_string('WB (R), M (RC)')), {'wbr', 'mr', 'mc'})

    def test_D_WB_R_DM(self):
        self.assertEqual(set(parse_position_string('D/WB (R), DM')), {'dr', 'wbr', 'dm'})

    def test_WB_RL_DM_M_C(self):
        self.assertEqual(set(parse_position_string('WB (RL), DM, M (C)')), {'wbr', 'wbl', 'dm', 'mc'})

    def test_WB_M_L(self):
        self.assertEqual(set(parse_position_string('WB/M (L)')), {'wbl', 'ml'})

    def test_WB_R_M_RL_AM_C(self):
        self.assertEqual(set(parse_position_string('WB (R), M (RL), AM (C)')), {'wbr', 'mr', 'ml', 'amc'})

    def test_D_WB_M_R_AM_L(self):
        self.assertEqual(set(parse_position_string('D/WB/M (R), AM (L)')), {'dr', 'wbr', 'mr', 'aml'})

    def test_WB_R_AM_C(self):
        self.assertEqual(set(parse_position_string('WB (R), AM (C)')), {'wbr', 'amc'})

    def test_WB_M_AM_L_ST_C(self):
        self.assertEqual(set(parse_position_string('WB/M/AM (L), ST (C)')), {'wbl', 'ml', 'aml', 'sc'})

    def test_WB_RL_M_AM_R(self):
        self.assertEqual(set(parse_position_string('WB (RL), M/AM (R)')), {'wbr', 'wbl', 'mr', 'amr'})

    def test_D_WB_L_M_C_AM_LC(self):
        self.assertEqual(set(parse_position_string('D/WB (L), M (C), AM (LC)')), {'dl', 'wbl', 'mc', 'aml', 'amc'})

    def test_D_WB_R_DM_M_RLC(self):
        self.assertEqual(set(parse_position_string('D/WB (R), DM, M (RLC)')), {'dr', 'wbr', 'dm', 'mr', 'ml', 'mc'})

    def test_D_R_M_C_AM_RC(self):
        self.assertEqual(set(parse_position_string('D (R), M (C), AM (RC)')), {'dr', 'mc', 'amr', 'amc'})

    def test_D_C_DM_M_LC_AM_C(self):
        self.assertEqual(set(parse_position_string('D (C), DM, M (LC), AM (C)')), {'dc', 'dm', 'ml', 'mc', 'amc'})

    def test_D_WB_L_M_AM_RL(self):
        self.assertEqual(set(parse_position_string('D/WB (L), M/AM (RL)')), {'dl', 'wbl', 'mr', 'ml', 'amr', 'aml'})

    def test_DM_M_C_AM_RL_ST_C(self):
        self.assertEqual(set(parse_position_string('DM, M (C), AM (RL), ST (C)')), {'dm', 'mc', 'aml', 'amr', 'sc'})

    def test_D_M_L_AM_RL_ST_C(self):
        self.assertEqual(set(parse_position_string('D/M (L), AM (RL), ST (C)')), {'dl', 'ml', 'aml', 'amr', 'sc'})

    def test_DM_M_R_AM_RL(self):
        self.assertEqual(set(parse_position_string('DM, M (R), AM (RL)')), {'dm', 'mr', 'aml', 'amr'})

    def test_M_RL_AM_R_ST_C(self):
        self.assertEqual(set(parse_position_string('M (RL), AM (R), ST (C)')), {'mr', 'ml', 'amr', 'sc'})

    def test_D_R_M_L_AM_RL(self):
        self.assertEqual(set(parse_position_string('D (R), M (L), AM (RL)')), {'dr', 'ml', 'aml', 'amr'})

    def test_D_LC_DM_M_LC_AM_C(self):
        self.assertEqual(set(parse_position_string('D (LC), DM, M (LC), AM (C)')), {'dl', 'dc', 'dm', 'ml', 'mc', 'amc'})

    def test_M_C_AM_L(self):
        self.assertEqual(set(parse_position_string('M (C), AM (L)')), {'mc', 'aml'})

    def test_WB_R_DM_M_RLC(self):
        self.assertEqual(set(parse_position_string('WB (R), DM, M (RLC)')), {'wbr', 'dm', 'mr', 'ml', 'mc'})

    def test_M_RC_AM_C_ST_C(self):
        self.assertEqual(set(parse_position_string('M (RC), AM (C), ST (C)')), {'mr', 'mc', 'amc', 'sc'})

    def test_D_L_WB_RL(self):
        self.assertEqual(set(parse_position_string('D (L), WB (RL)')), {'dl', 'wbr', 'wbl'})

    def test_D_WB_M_L_AM_RL_ST_C(self):
        self.assertEqual(set(parse_position_string('D/WB/M (L), AM (RL), ST (C)')), {'dl', 'wbl', 'ml', 'aml', 'amr', 'sc'})

    def test_M_L_AM_R_ST_C(self):
        self.assertEqual(set(parse_position_string('M (L), AM (R), ST (C)')), {'ml', 'amr', 'sc'})

    def test_WB_L_M_RC_AM_C(self):
        self.assertEqual(set(parse_position_string('WB (L), M (RC), AM (C)')), {'wbl', 'mr', 'mc', 'amc'})

    def test_D_C_WB_R_DM_M_RC(self):
        self.assertEqual(set(parse_position_string('D (C), WB (R), DM, M (RC)')), {'dc', 'wbr', 'dm', 'mr', 'mc'})


if __name__ == '__main__':
    unittest.main()
