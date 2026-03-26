import time

def simulate(r):
    r.setIntegrator('cvode')
    r.integrator.absolute_tolerance = 1e-14
    r.integrator.relative_tolerance = 1e-12
    r.integrator.setValue('stiff', True)
    r.integrator.variable_step_size = True
    print(r.integrator)

    observed_species = ['time','[AB42_Plasma]', '[Antibody_Plasma]',
    '[AB42__Antibody_Plasma]', '[AB42_Oligomer_Plasma]',
    '[AB42_Oligomer__Antibody_Plasma]','[AB42_BrainISF]',
     '[AB42_Plaque_BrainISF]', '[AB42_Plaque__Antibody_BrainISF]', 
     '[AB42_Plaque__Antibody__FcR_BrainISF]', 
     '[AB42_Oligomer_BrainISF]', '[AB42_Oligomer__Antibody_BrainISF]',
     '[AB42_CSF]', '[AB42_Oligomer_CSF]',
     '[AB42_Oligomer__Antibody_CSF]',
     'totalmAbPlasma', 'totalmAbCSF', 'totalAbetaPlasma', 'totalPlaque', 'totaloligISF',
     'AB42_Plasma', 'Antibody_Plasma',
    'AB42__Antibody_Plasma', 'AB42_Oligomer_Plasma',
    'AB42_Oligomer__Antibody_Plasma',
    'AB42_CSF', 'Antibody_CSF',
    'AB42__Antibody_CSF', 'AB42_Oligomer_CSF',
    'AB42_Oligomer__Antibody_CSF',
    'AB42_BrainISF', 'Antibody_BrainISF',
    'AB42__Antibody_BrainISF', 'AB42_Oligomer_BrainISF',
    'AB42_Oligomer__Antibody_BrainISF',
    'totaloligPlasma', 'totalAbetaBrainISF'
     
     ]


    print("Running simulation...")
    t0 = time.perf_counter()

    result0 = r.simulate(0, 7257600 , 1000000, observed_species)
    
    elapsed = time.perf_counter() - t0
    print(f"Simulation time: {elapsed:.3f} s")
    print(f"CVODE took {len(result0)} steps.")

    return result0
