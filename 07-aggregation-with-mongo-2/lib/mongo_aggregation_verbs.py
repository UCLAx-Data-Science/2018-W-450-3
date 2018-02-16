PROJECT = "$project"
MATCH = "$match"
LIMIT = "$limit"
UNWIND = "$unwind"
GROUP = "$group"
SORT = "$sort"
COUNT = "$count"

greater_than_10 = { "$gt" : 10}
not_an_empty_array = { "$ne" : [] }
sum_1 = { "$sum" : 1 }

count_geo = { COUNT : "geo"}
match_count_gt = { MATCH : { "count" : greater_than_10 } }
match_non_empty_hashtag_arrays = { MATCH : { "entities.hashtags" : not_an_empty_array}}
match_non_null_geo = { MATCH : { "geo" : { "$ne" : None }}}
project_to_text_only = { PROJECT : { "text" : "$entities.hashtags.text", "_id" :0 }}
project_to_lower = { PROJECT : { "text" : {"$toLower" : "$text"} } }
sort_by_count = { SORT : {"count" : -1}}
unwind_text = { UNWIND : "$text" }

def group_and_count(key):
    return { GROUP : {
                 "_id" : key,
                 "count" : sum_1
                }
           }

def limit(val):
    return { LIMIT : val }
