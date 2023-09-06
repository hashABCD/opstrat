import opstrat as op

op1={'op_type': 'c', 'strike': 215, 'tr_type': 's', 'op_pr': 7.63, 'contract': 1, 'exp_date':'15-Sep-23'}
op2={'op_type': 'p', 'strike': 220, 'tr_type': 'b', 'op_pr': 5.35, 'contract': 1, 'exp_date':'15-Sep-23'}
# op3={'op_type': 'p', 'strike': 210, 'tr_type': 's', 'op_pr': 7.20, 'contract': 1, 'exp_date':'08-Sep-23'}
# op4={'op_type': 'p', 'strike': 205, 'tr_type': 'b', 'op_pr': 5.52, 'contract': 1, 'exp_date':'15-Sep-23'}
# op5={'op_type': 's', 'strike': 210, 'tr_type': 'b', 'op_pr': 0, 'contract': 50}

op_list=[op1
        , op2
        # , op3
        # , op4
        # , op5
         ]
op.multi_plotter(spot=212.26,spot_range=10, exp_adjust=9, op_list=op_list)

# op.single_plotter(spot=212.26, spot_range=10, strike=210, op_type='s', tr_type='s', op_pr=0)
# op.single_plotter(spot=212.26, spot_range=10, strike=210, op_type='s', tr_type='b', op_pr=0)