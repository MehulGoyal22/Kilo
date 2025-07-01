varied_simembed_dict = {}
sim_path = '/home/oppenheimer/summer2025/Kilo/data/lc_dir'
num_sims = 25000

simembed_num_lc_list = [24750, 25000, 25000, 25000, 25000, 25000, 24850, 25000, 25000, 25000]

for i in range (0, 10):
    # get the names of each file
    file_names = get_names(sim_path, 'varied', i, simembed_num_lc_list[i])
    # open the files as dataframes
    varied_simembed_dict['varied_simembed_data_{}'.format(i)] = json_to_df(file_names, simembed_num_lc_list[i])
    # pad the data
    varied_simembed_dict['varied_simembed_data_{}'.format(i)] = pad_all_dfs(varied_simembed_dict['varied_simembed_data_{}'.format(i)])

varied_simembed_dict['varied_simembed_data_0'][-1]

# plot a small sample of the varied light curves

for i in range(0, 300, 50):
    plt.scatter(varied_simembed_dict['varied_simembed_data_0'][i]['t'], varied_simembed_dict['varied_simembed_data_0'][i]['ztfg'], color = 'g')
    plt.scatter(varied_simembed_dict['varied_simembed_data_0'][i]['t'], varied_simembed_dict['varied_simembed_data_0'][i]['ztfr'], color = 'r')
    plt.scatter(varied_simembed_dict['varied_simembed_data_0'][i]['t'], varied_simembed_dict['varied_simembed_data_0'][i]['ztfi'], color = 'c')
plt.gca().invert_yaxis()
plt.xlabel('Time (days)')
plt.ylabel('Magnitude')



