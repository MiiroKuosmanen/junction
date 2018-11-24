import pandas as pd
import matplotlib
import numpy as np
import seaborn as sns
import random

# filter by attributes
# calc prob of drawing sample
# if drawn, draw receipt and skip next day
# if not drawn, proceed to next day
def gen_customers(df, num_customers, PersonAge, KCust, Qual, Easy):

    ## TODO: handle edge cases

    pop = df.loc[(df['KCustomer'] == KCust) &(df['PersonAgeGrp'] == PersonAge) &(df['QualClass'] ==  Qual) &(df['EasyClass'] ==  Easy)]
    #create empty dict for customers
    customer_samples = dict()

    #create empty list to ensure we dont sample same receipts
    used_receipts = []
    for i in range(num_customers):
        pop = pop.loc[~pop['Receipt'].isin(used_receipts)]

        #create empty entry for a customer sample
        customer_samples[i] = []

        #know date range
        dates = sorted(list(set(pop['TransactionDate'])))

        j = 0
        for date in dates:
            try:
                new_pop = pop.loc[pop['TransactionDate'] == date]
                new_pop = new_pop.loc[~new_pop['Receipt'].isin(used_receipts)]
                if np.random.binomial(1, 0.6, size=1)[0] == 1:
                    receipt_sample = random.sample(set(new_pop['Receipt']), 1)
                    used_receipts.extend(receipt_sample)
                    customer_samples[i].extend(receipt_sample)
                else:
                    pass
            except:
                pass
    return(customer_samples)



def produce_customer_profile(df_list, num_iter, num_customers, PersonAge, KCust, Qual, Easy):
    master_customer_dfs = dict()

    for customer in range(num_customers):
        master_customer_dfs[customer] = []

    for i in range(num_iter):
        try:
            df = df_list.get_chunk()
            receipt_ids = gen_customers(df, num_customers, PersonAge, KCust, Qual, Easy)
            for customer_id in receipt_ids:
                master_customer_dfs[customer_id].append(df.loc[df['Receipt'].isin(receipt_ids[customer_id])])
            print(i, end='')

        except:
            print(i, end='')

    return(master_customer_dfs)

def create_master_dataframe(customer_dfs_dict, id_offset):
    output = []
    for customer_id in customer_dfs_dict:
        df= pd.concat(customer_dfs_dict[customer_id])
        df['CustomerID'] = customer_id + id_offset
        output.append(df)
    return(pd.concat(output))

age_ranges = ['18-24', '25-34', '35-44', '45-54', '55-64', '65-']
Kcustomer_types = [6711, 6712, 6713, 6714, 6715]
QualClass_types = ['Q_1-3', 'Q_4-7', 'Q_8-10']
EasyClass_types = ['E_1-3', 'E_4-7', 'E_8-10']

offset = 0 # 225 + 225 + 225 +225 # if doing one age_range at a time before ending script

for age in age_ranges:
    for kcust in Kcustomer_types:
        for qual in QualClass_types:
            for easy in EasyClass_types:
                print('|'.join([str(age),str(kcust),str(qual),str(easy)]))
                df_list = pd.read_csv("junction/Junction_Data.csv", delimiter=';', chunksize=3000000, decimal=',')
                master_customer_dfs = produce_customer_profile(df_list, num_iter=35, num_customers=5, PersonAge=age, KCust=kcust, Qual=qual, Easy=easy)
                master_df = create_master_dataframe(master_customer_dfs, offset)
                filename = "customers_" + str(offset) +"_" + str(offset + 4) + ".csv"
                master_df.to_csv(filename, index=False)
                offset += 5
                print("")
