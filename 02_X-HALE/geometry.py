# Lifting segments  
lifting_segments = []

# Lifting segment #1 
lifting_segments.append({'segment_name'                  : 'wing_right',          \
                         'point1'                        : np.array([[-0.05734,  0.,      0.005]]), \
                         'point2'                        : np.array([[-0.05734,  2.9839,  0.17859]]), \
                         'point3'                        : np.array([[ 0.1419,   2.987,   0.16143]]), \
                         'point4'                        : np.array([[ 0.1419,   0.,     -0.01241]]), \
                         'intermediate_points'           : np.array([[-0.05734,  1.,      0.00502],   \
                                                                     [-0.05734,  2.,      0.00502], \
                                                                     [ 0.1419,   2.,     -0.01241], \
                                                                     [ 0.1419,   1.,     -0.01241]]), \
                         'no_panels_span_intermediate'   : [18, 18, 18], \
                         'no_panels_chord'               : 16,              \
                         'sine_spacing'                  : 0,              \
                         'spanwise_spacing'              : np.array([-(3.*np.pi)/8., np.pi/2]), \
                         'chordwise_spacing'             : np.array([-(7.*np.pi)/16., (3.*np.pi)/8]), \
                         'spanwise_spacing_intermediate' : np.array([[-np.pi/2., np.pi/2],  \
                                                                     [-np.pi/2., np.pi/2],  \
                                                                     [-np.pi/2., np.pi/2]]), \
                         'filename_airfoil_14'           : './emx07_fine.dat', \
                         'filename_airfoil_23'           : './emx07_fine.dat', \
                         'filename_airfoil_intermediate' : ['./emx07_fine.dat', './emx07_fine.dat']})
# Lifting segment #2
lifting_segments.append({'segment_name'                  : 'wing_left',          \
                         'point1'                        : np.array([[-0.05734,  -2.9839,  0.17859]]), \
                         'point2'                        : np.array([[-0.05734,   0.,      0.005]]), \
                         'point3'                        : np.array([[ 0.1419,    0.,     -0.01241]]), \
                         'point4'                        : np.array([[ 0.1419,   -2.987,   0.16143]]), \
                         'intermediate_points'           : np.array([[-0.05734,  -2.,      0.00502], \
                                                                     [-0.05734,  -1.,      0.00502], \
                                                                     [ 0.1419,   -1.,     -0.01241],   \
                                                                     [0.1419,    -2.,     -0.01241]]), \
                         'no_panels_span_intermediate'   : [18, 18, 18], \
                         'no_panels_chord'               : 16,              \
                         'sine_spacing'                  : 0,              \
                         'spanwise_spacing'              : np.array([-(3.*np.pi)/8., np.pi/2]), \
                         'chordwise_spacing'             : np.array([-(7.*np.pi)/16., (3.*np.pi)/8]), \
                         'spanwise_spacing_intermediate' : np.array([[-np.pi/2., np.pi/2],  \
                                                                     [-np.pi/2., np.pi/2],  \
                                                                     [-np.pi/2., np.pi/2]]), \
                         'filename_airfoil_14'           : './emx07_fine.dat', \
                         'filename_airfoil_23'           : './emx07_fine.dat', \
                         'filename_airfoil_intermediate' : ['./emx07_fine.dat', './emx07_fine.dat']})
# Lifting segment #3
lifting_segments.append({'segment_name'                  : 'PODC',          \
                         'point1'                        : np.array([[-0.231534,  0.0, -0.184]]), \
                         'point2'                        : np.array([[-0.231534,  0.0,  0.]]), \
                         'point3'                        : np.array([[ 0.148466,  0.0,  0.]]), \
                         'point4'                        : np.array([[ 0.148466,  0.0, -0.184]]), \
                         'no_panels_span'                : 2, \
                         'no_panels_chord'               : 2,              \
                         'sine_spacing'                  : 0})
# Lifting segment #4
lifting_segments.append({'segment_name'                  : 'POD2up',          \
                         'point1'                        : np.array([[-0.231534,  1., -0.184]]), \
                         'point2'                        : np.array([[-0.231534,  1.,  0.]]), \
                         'point3'                        : np.array([[ 0.148466,  1.,  0.]]), \
                         'point4'                        : np.array([[ 0.148466,  1., -0.184]]), \
                         'no_panels_span'                : 2, \
                         'no_panels_chord'               : 2,              \
                         'sine_spacing'                  : 0})
# Lifting segment #5
lifting_segments.append({'segment_name'                  : 'POD4up',          \
                         'point1'                        : np.array([[-0.231534,  2., -0.184]]), \
                         'point2'                        : np.array([[-0.231534,  2.,  0.]]), \
                         'point3'                        : np.array([[ 0.148466,  2.,  0.]]), \
                         'point4'                        : np.array([[ 0.148466,  2., -0.184]]), \
                         'no_panels_span'                : 2, \
                         'no_panels_chord'               : 2,              \
                         'sine_spacing'                  : 0})
# Lifting segment #6
lifting_segments.append({'segment_name'                  : 'POD1up',          \
                         'point1'                        : np.array([[-0.231534,  -1., -0.184]]), \
                         'point2'                        : np.array([[-0.231534,  -1.,  0.]]), \
                         'point3'                        : np.array([[ 0.148466,  -1.,  0.]]), \
                         'point4'                        : np.array([[ 0.148466,  -1., -0.184]]), \
                         'no_panels_span'                : 2, \
                         'no_panels_chord'               : 2, \
                         'sine_spacing'                  : 0})
# Lifting segment #7
lifting_segments.append({'segment_name'                  : 'POD3up',          \
                         'point1'                        : np.array([[-0.231534,  -2., -0.184]]), \
                         'point2'                        : np.array([[-0.231534,  -2.,  0.]]), \
                         'point3'                        : np.array([[ 0.148466,  -2.,  0.]]), \
                         'point4'                        : np.array([[ 0.148466,  -2., -0.184]]), \
                         'no_panels_span'                : 2, \
                         'no_panels_chord'               : 2, \
                         'sine_spacing'                  : 0})
# Lifting segment #8
lifting_segments.append({'segment_name'                  : 'CtailL',          \
                         'point1'                        : np.array([[1.070415, 0., -0.145]]), \
                         'point2'                        : np.array([[1.070415, 0.,  0.]]), \
                         'point3'                        : np.array([[1.180415, 0.,  0.]]), \
                         'point4'                        : np.array([[1.180415, 0., -0.145]]), \
                         'no_panels_span'                : 3, \
                         'no_panels_chord'               : 3, \
                         'sine_spacing'                  : 0})
# Lifting segment #9
lifting_segments.append({'segment_name'                  : 'CtailR',          \
                         'point1'                        : np.array([[1.070415, 0., 0.]]), \
                         'point2'                        : np.array([[1.070415, 0., 0.24]]), \
                         'point3'                        : np.array([[1.180415, 0., 0.24]]), \
                         'point4'                        : np.array([[1.180415, 0., 0.]]), \
                         'no_panels_span'                : 3, \
                         'no_panels_chord'               : 3, \
                         'sine_spacing'                  : 0})
# Lifting segment #10
lifting_segments.append({'segment_name'                  : 'TR1in',          \
                         'point1'                        : np.array([[0.614415,  0.76, 0.]]), \
                         'point2'                        : np.array([[0.614415,  1.,   0.]]), \
                         'point3'                        : np.array([[0.724415,  1.,   0.]]), \
                         'point4'                        : np.array([[0.724415,  0.76, 0.]]), \
                         'no_panels_span'                : 3, \
                         'no_panels_chord'               : 3,              \
                         'flap_panels_span'              : [0,3],            \
                         'flap_panels_chord'             : [0,3],            \
                         'sine_spacing'                  : 0, \
                         'hinge_line_points'             : np.array([[0.65, -1., 0.], \
                                                                     [0.65,  1., 0.]])})
# Lifting segment #11
lifting_segments.append({'segment_name'                  : 'TR1ou',          \
                         'point1'                        : np.array([[0.614415,  1.,   0.]]), \
                         'point2'                        : np.array([[0.614415,  1.24, 0.]]), \
                         'point3'                        : np.array([[0.724415,  1.24, 0.]]), \
                         'point4'                        : np.array([[0.724415,  1.,   0.]]), \
                         'no_panels_span'                : 3, \
                         'no_panels_chord'               : 3,              \
                         'flap_panels_span'              : [0,3],            \
                         'flap_panels_chord'             : [0,3],            \
                         'sine_spacing'                  : 0, \
                         'hinge_line_points'             : np.array([[0.65, -1., 0.], \
                                                                     [0.65,  1., 0.]])})
# Lifting segment #12
lifting_segments.append({'segment_name'                  : 'TR2in',          \
                         'point1'                        : np.array([[0.614415,  1.76, 0.]]), \
                         'point2'                        : np.array([[0.614415,  2.,   0.]]), \
                         'point3'                        : np.array([[0.724415,  2.,   0.]]), \
                         'point4'                        : np.array([[0.724415,  1.76, 0.]]), \
                         'no_panels_span'                : 3, \
                         'no_panels_chord'               : 3,              \
                         'flap_panels_span'              : [0,3],            \
                         'flap_panels_chord'             : [0,3],            \
                         'sine_spacing'                  : 0, \
                         'hinge_line_points'             : np.array([[0.65, -1., 0.], \
                                                                     [0.65,  1., 0.]])})
# Lifting segment #13
lifting_segments.append({'segment_name'                  : 'TR2ou',          \
                         'point1'                        : np.array([[0.614415,  2.,   0.]]), \
                         'point2'                        : np.array([[0.614415,  2.24, 0.]]), \
                         'point3'                        : np.array([[0.724415,  2.24, 0.]]), \
                         'point4'                        : np.array([[0.724415,  2.,   0.]]), \
                         'no_panels_span'                : 3, \
                         'no_panels_chord'               : 3,              \
                         'flap_panels_span'              : [0,3],            \
                         'flap_panels_chord'             : [0,3],            \
                         'sine_spacing'                  : 0, \
                         'hinge_line_points'             : np.array([[0.65, -1., 0.], \
                                                                     [0.65,  1., 0.]])})
# Lifting segment #14
lifting_segments.append({'segment_name'                  : 'TL1in',          \
                         'point1'                        : np.array([[0.614415,  -1.,   0.]]), \
                         'point2'                        : np.array([[0.614415,  -0.76, 0.]]), \
                         'point3'                        : np.array([[0.724415,  -0.76, 0.]]), \
                         'point4'                        : np.array([[0.724415,  -1.,   0.]]), \
                         'no_panels_span'                : 3, \
                         'no_panels_chord'               : 3,              \
                         'flap_panels_span'              : [0,3],            \
                         'flap_panels_chord'             : [0,3],            \
                         'sine_spacing'                  : 0, \
                         'hinge_line_points'             : np.array([[0.65, -1., 0.], \
                                                                     [0.65,  1., 0.]])})
# Lifting segment #15
lifting_segments.append({'segment_name'                  : 'TL1ou',          \
                         'point1'                        : np.array([[0.614415,  -1.24, 0.]]), \
                         'point2'                        : np.array([[0.614415,  -1.,   0.]]), \
                         'point3'                        : np.array([[0.724415,  -1.,   0.]]), \
                         'point4'                        : np.array([[0.724415,  -1.24, 0.]]), \
                         'no_panels_span'                : 3, \
                         'no_panels_chord'               : 3,              \
                         'flap_panels_span'              : [0,3],            \
                         'flap_panels_chord'             : [0,3],            \
                         'sine_spacing'                  : 0, \
                         'hinge_line_points'             : np.array([[0.65, -1., 0.], \
                                                                     [0.65,  1., 0.]])})
# Lifting segment #16
lifting_segments.append({'segment_name'                  : 'TL2in',          \
                         'point1'                        : np.array([[0.614415,  -2.,   0.]]), \
                         'point2'                        : np.array([[0.614415,  -1.76, 0.]]), \
                         'point3'                        : np.array([[0.724415,  -1.76, 0.]]), \
                         'point4'                        : np.array([[0.724415,  -2.,   0.]]), \
                         'no_panels_span'                : 3, \
                         'no_panels_chord'               : 3,              \
                         'flap_panels_span'              : [0,3],            \
                         'flap_panels_chord'             : [0,3],            \
                         'sine_spacing'                  : 0, \
                         'hinge_line_points'             : np.array([[0.65, -1., 0.], \
                                                                     [0.65,  1., 0.]])})
# Lifting segment #17
lifting_segments.append({'segment_name'                  : 'TL2ou',          \
                         'point1'                        : np.array([[0.614415,  -2.24,  0.]]), \
                         'point2'                        : np.array([[0.614415,  -2.,    0.]]), \
                         'point3'                        : np.array([[0.724415,  -2.,    0.]]), \
                         'point4'                        : np.array([[0.724415,  -2.24,  0.]]), \
                         'no_panels_span'                : 3, \
                         'no_panels_chord'               : 3,              \
                         'flap_panels_span'              : [0,3],            \
                         'flap_panels_chord'             : [0,3],            \
                         'sine_spacing'                  : 0, \
                         'hinge_line_points'             : np.array([[0.65, -1., 0.], \
                                                                     [0.65,  1., 0.]])})
# Lifting segment #18
lifting_segments.append({'segment_name'                  : 'CFin',          \
                         'point1'                        : np.array([[ 0.15,  0.01, -0.14]]), \
                         'point2'                        : np.array([[ 0.15,  0.01,  0.01]]), \
                         'point3'                        : np.array([[ 0.93,  0.01,  0.01]]), \
                         'point4'                        : np.array([[ 0.93,  0.01, -0.14]]), \
                         'no_panels_span'                : 2, \
                         'no_panels_chord'               : 4, \
                         'sine_spacing'                  : 0})
# Lifting segment #19
lifting_segments.append({'segment_name'                  : 'RFin',          \
                         'point1'                        : np.array([[ 0.16,   1.01, -0.14]]), \
                         'point2'                        : np.array([[ 0.16,   1.01,  0.01]]), \
                         'point3'                        : np.array([[ 0.59,   1.01,  0.01]]), \
                         'point4'                        : np.array([[ 0.59,   1.01, -0.14]]), \
                         'no_panels_span'                : 2, \
                         'no_panels_chord'               : 4, \
                         'sine_spacing'                  : 0})
# Lifting segment #20
lifting_segments.append({'segment_name'                  : 'LFin',          \
                         'point1'                        : np.array([[ 0.16,   -1.01, -0.14]]), \
                         'point2'                        : np.array([[ 0.16,   -1.01,  0.01]]), \
                         'point3'                        : np.array([[ 0.59,   -1.01,  0.01]]), \
                         'point4'                        : np.array([[ 0.59,   -1.01, -0.14]]), \
                         'no_panels_span'                : 2, \
                         'no_panels_chord'               : 4, \
                         'sine_spacing'                  : 0})

self.lifting_segments = lifting_segments
