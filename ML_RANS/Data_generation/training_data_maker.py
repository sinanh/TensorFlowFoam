import numpy as np


def replaceZeroes(data):
    min_nonzero = np.min(data[np.nonzero(data)])
    data[data == 0] = min_nonzero
    return data

LINE = 21

def read_scalar(filename):
    # Read file
    file = open(filename,'r')
    lines_1 = file.readlines()
    file.close()

    num_cells_internal = int(lines_1[LINE].strip('\n'))
    lines_1 = lines_1[LINE+2:LINE+2+num_cells_internal]

    for i in range(len(lines_1)):
        lines_1[i] = lines_1[i].strip('\n')

    field = np.asarray(lines_1).astype('double').reshape(num_cells_internal,1)
    field = replaceZeroes(field)

    return field


def read_vector(filename): # Only x,y components
    file = open(filename,'r')
    lines_1 = file.readlines()
    file.close()

    num_cells_internal = int(lines_1[LINE].strip('\n'))
    lines_1 = lines_1[LINE+2:LINE+2+num_cells_internal]

    for i in range(len(lines_1)):
        lines_1[i] = lines_1[i].strip('\n')
        lines_1[i] = lines_1[i].strip('(')
        lines_1[i] = lines_1[i].strip(')')
        lines_1[i] = lines_1[i].split()

    field = np.asarray(lines_1).astype('double')[:,:2]

    return field


if __name__ == '__main__':
    print('Velocity reader file')

    # Read Case 1
    U = read_vector('U_1')
    nut = read_scalar('nut_1')
    y = read_scalar('yWall_1')
    cx = read_scalar('Cx_1')
    cy = read_scalar('Cy_1')
    # create array of Re information
    h = np.ones(shape=(np.shape(U)[0],1),dtype='double')*0.127
    total_dataset = np.concatenate((U,cx,cy,h,nut),axis=-1)

    # Read Case 2
    U = read_vector('U_2')
    nut = read_scalar('nut_2')
    y = read_scalar('yWall_2')
    cx = read_scalar('Cx_2')
    cy = read_scalar('Cy_2')
    # create array of Re information
    h = np.ones(shape=(np.shape(U)[0],1),dtype='double')*0.127
    temp_dataset = np.concatenate((U,cx,cy,h,nut),axis=-1)
    total_dataset = np.concatenate((total_dataset,temp_dataset),axis=0)

    # Read Case 3
    U = read_vector('U_3')
    nut = read_scalar('nut_3')
    y = read_scalar('yWall_3')
    cx = read_scalar('Cx_3')
    cy = read_scalar('Cy_3')
    # create array of Re information
    h = np.ones(shape=(np.shape(U)[0],1),dtype='double')*0.127
    temp_dataset = np.concatenate((U,cx,cy,h,nut),axis=-1)
    total_dataset = np.concatenate((total_dataset,temp_dataset),axis=0)

    # Read Case 4
    U = read_vector('U_4')
    nut = read_scalar('nut_4')
    y = read_scalar('yWall_4')
    cx = read_scalar('Cx_4')
    cy = read_scalar('Cy_4')
    # create array of Re information
    h = np.ones(shape=(np.shape(U)[0],1),dtype='double')*0.127
    temp_dataset = np.concatenate((U,cx,cy,h,nut),axis=-1)
    total_dataset = np.concatenate((total_dataset,temp_dataset),axis=0)

    # Read Case 5
    U = read_vector('U_5')
    nut = read_scalar('nut_5')
    y = read_scalar('yWall_5')
    cx = read_scalar('Cx_5')
    cy = read_scalar('Cy_5')
    # create array of Re information
    h = np.ones(shape=(np.shape(U)[0],1),dtype='double')*0.127
    temp_dataset = np.concatenate((U,cx,cy,h,nut),axis=-1)
    total_dataset = np.concatenate((total_dataset,temp_dataset),axis=0)

    # Read Case 6
    U = read_vector('U_6')
    nut = read_scalar('nut_6')
    y = read_scalar('yWall_6')
    cx = read_scalar('Cx_6')
    cy = read_scalar('Cy_6')
    # create array of Re information
    h = np.ones(shape=(np.shape(U)[0],1),dtype='double')*0.127
    temp_dataset = np.concatenate((U,cx,cy,h,nut),axis=-1)
    total_dataset = np.concatenate((total_dataset,temp_dataset),axis=0)

    # Read Case 7
    U = read_vector('U_7')
    nut = read_scalar('nut_7')
    y = read_scalar('yWall_7')
    cx = read_scalar('Cx_7')
    cy = read_scalar('Cy_7')
    # create array of Re information
    h = np.ones(shape=(np.shape(U)[0],1),dtype='double')*0.127
    temp_dataset = np.concatenate((U,cx,cy,h,nut),axis=-1)
    total_dataset = np.concatenate((total_dataset,temp_dataset),axis=0)

    # Read Case 8
    U = read_vector('U_8')
    nut = read_scalar('nut_8')
    y = read_scalar('yWall_8')
    cx = read_scalar('Cx_8')
    cy = read_scalar('Cy_8')
    # create array of Re information
    h = np.ones(shape=(np.shape(U)[0],1),dtype='double')*0.127
    temp_dataset = np.concatenate((U,cx,cy,h,nut),axis=-1)
    total_dataset = np.concatenate((total_dataset,temp_dataset),axis=0)

    # Read Case 9
    U = read_vector('U_9')
    nut = read_scalar('nut_9')
    y = read_scalar('yWall_9')
    cx = read_scalar('Cx_9')
    cy = read_scalar('Cy_9')
    # create array of Re information
    h = np.ones(shape=(np.shape(U)[0],1),dtype='double')*0.127
    temp_dataset = np.concatenate((U,cx,cy,h,nut),axis=-1)
    total_dataset = np.concatenate((total_dataset,temp_dataset),axis=0)

    # Read Case 10
    U = read_vector('U_10')
    nut = read_scalar('nut_10')
    y = read_scalar('yWall_10')
    cx = read_scalar('Cx_10')
    cy = read_scalar('Cy_10')
    # create array of Re information
    h = np.ones(shape=(np.shape(U)[0],1),dtype='double')*0.127
    temp_dataset = np.concatenate((U,cx,cy,h,nut),axis=-1)
    total_dataset = np.concatenate((total_dataset,temp_dataset),axis=0)

    # Read Case 11
    U = read_vector('U_11')
    nut = read_scalar('nut_11')
    y = read_scalar('yWall_11')
    cx = read_scalar('Cx_11')
    cy = read_scalar('Cy_11')
    # create array of Re information
    h = np.ones(shape=(np.shape(U)[0],1),dtype='double')*0.127
    temp_dataset = np.concatenate((U,cx,cy,h,nut),axis=-1)
    total_dataset = np.concatenate((total_dataset,temp_dataset),axis=0)

    print(total_dataset.shape)

    # Save data   
    np.save('Total_dataset.npy',total_dataset)

    # Save the statistics of the data
    means = np.mean(total_dataset,axis=0).reshape(1,np.shape(total_dataset)[1])
    stds = np.std(total_dataset,axis=0).reshape(1,np.shape(total_dataset)[1])

    # Concatenate
    op_data = np.concatenate((means,stds),axis=0)
    np.savetxt('means',op_data, delimiter=' ')

    # Need to write out in OpenFOAM rectangular matrix format

    print('Means:')
    print(means)
    print('Stds:')
    print(stds)
