import Orange
data = Orange.data.Table("freqItemList/input_data.csv")
#mine rule from frequent itemset
rules = Orange.associate.AssociationRulesSparseInducer(data, support=0.5)
print("%4s %4s  %s" % ("Supp", "Conf", "Rule"))
for r in rules[:5]:
    print("%4.1f %4.1f  %s" % (r.support, r.confidence, r))