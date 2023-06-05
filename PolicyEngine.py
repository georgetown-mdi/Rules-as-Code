def formula(spm_unit, period, parameters):
  programs = parameters(period).gov.usda.snap.categorical_eligibility
  return add(spm_unit, period, programs) > 0