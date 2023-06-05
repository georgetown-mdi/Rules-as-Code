def formula(spm_unit, period, parameters):
  limit = parameters(period).gov.usda.snap.income.limit.gross
  income = spm_unit("snap_gross_income_fpg_ratio", period)
  has_elderly_disabled = spm_unit("has_usda_elderly_disabled", period)
  return has_elderly_disabled | (income <= limit)