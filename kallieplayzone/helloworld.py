'''
Created on Aug 6, 2018

@author: Kallie.Goodwin
'''
# single line comments
''' 
multi-line comment 
'''

import kallieplayzone as kpz #import as 
import figendpoint.qb_portfolio as qbp
import qbaccess as qba



if __name__=='__main__': 
   
    print ("hello world")
    j = 6
    k = 8
    z = kpz.add_nums(j, k)
    print z
    
    firstname = "kallie" 
    lastname = "goodwin"
    n = kpz.add_names(firstname,lastname)
    print n 
    
    qbs = qbp.QbStaging()
    bst = qbs.qbt_bs_staging
    #q = "{'23'.CT.'20180806'}AND{'9'.CT.'4'}"
    q1 = "{'23'.CT.'20180806'}"
    q2 = "{'9'.CT.'4'}"
    q = "AND".join([q1,q2])
    df = bst.get_bq(query = q, return_field_number_string="22.3.6.11.9.7.10.25.8.4.5.14.13.15.12.40.16.23.24.21.20.27.28.31.29.30.1.2.33")
    df.to_csv(path_or_buf="qbfile.csv")
    print df
    
    
    
    