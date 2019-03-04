from Stackoverflow import test1 as testimpl
from Stackoverflow.TopicModeling import tp as tpmodeling
from Stackoverflow.nlp import SentimentAnalysisImpl as stimpl
from Stackoverflow.nlp import SentimentAnalysisImpl as stimpl


# file_path_for_answer_posts='C:/Users/pc/Desktop/FYP data/SSE_data/sse_users.csv'
# column_name_for_user_id='Id'
# rows = tec_skills.get_user_deatils(file_path_for_answer_posts,column_name_for_user_id)
#
#
# file_path_for_answer_posts='C:/Users/pc/Desktop/FYP data/SSE_data/sse_answer_posts.csv'
# column_name_for_user_id='OwnerUserId'
# count_type='answer_posts'
# text_column_name='Body'
# print('==========================================================================================')
# data=stimpl.get_avg_word_count_user_wise(file_path_for_answer_posts, column_name_for_user_id,count_type,text_column_name)
# print('**********************************   START   *******************************************')
# stimpl.cluster_data('avg_word_count_answer_posts',data)
# print('**********************************   END   *******************************************')
#
# file_path_for_answer_posts='C:/Users/pc/Desktop/FYP data/SSE_data/sse_question_posts.csv'
# column_name_for_user_id='OwnerUserId'
# count_type='answer_posts'
# text_column_name='Body'
# print('==========================================================================================')
# data=stimpl.get_avg_word_count_user_wise(file_path_for_answer_posts, column_name_for_user_id,count_type,text_column_name)
# print('**********************************   START   *******************************************')
# stimpl.cluster_data('avg_word_count_question_posts',data)
# print('**********************************   END   *******************************************')
#
#
# file_path_for_answer_posts='C:/Users/pc/Desktop/FYP data/SSE_data/sse_answer_posts.csv'
# column_name_for_user_id='OwnerUserId'
# count_type='answer_posts'
# text_column_name='Body'
# print('==========================================================================================')
# data2=stimpl.get_avg_sentences_count_user_wise(file_path_for_answer_posts, column_name_for_user_id,count_type,text_column_name)
# print('**********************************   START   *******************************************')
# stimpl.cluster_data('avg_setence_count_answer_posts',data2)
# print('**********************************   END   *******************************************')
#
# file_path_for_answer_posts='C:/Users/pc/Desktop/FYP data/SSE_data/sse_question_posts.csv'
# column_name_for_user_id='OwnerUserId'
# count_type='answer_posts'
# text_column_name='Body'
# print('==========================================================================================')
# data2=stimpl.get_avg_sentences_count_user_wise(file_path_for_answer_posts, column_name_for_user_id,count_type,text_column_name)
# print('**********************************   START   *******************************************')
# stimpl.cluster_data('avg_setence_count_question_posts',data2)
# print('**********************************   END   *******************************************')
#
#
# file_path_for_answer_posts='C:/Users/pc/Desktop/FYP data/SSE_data/sse_comments.csv'
# column_name_for_user_id='UserId'
# count_type='comments'
# text_column_name='Text'
# print('==========================================================================================')
# data=stimpl.get_avg_word_count_user_wise(file_path_for_answer_posts, column_name_for_user_id,count_type,text_column_name)
# print('**********************************   START   *******************************************')
# stimpl.cluster_data('avg_word_count_comments',data)
# print('**********************************   END   *******************************************')
#
#
# print('=================== Answer post counts user wise ==================================================================================')
# file_path_for_answer_posts='C:/Users/pc/Desktop/FYP data/SSE_data/sse_comments.csv'
# column_name_for_user_id='UserId'
# count_type='answer_posts'
# text_column_name='Text'
# print('==========================================================================================')
# data2=stimpl.get_avg_sentences_count_user_wise(file_path_for_answer_posts, column_name_for_user_id,count_type,text_column_name)
# print('**********************************   START   *******************************************')
# stimpl.cluster_data('avg_setence_count_comments',data2)
# print('**********************************   END   *******************************************')
#
# file_path_for_answer_posts='C:/Users/pc/Desktop/FYP data/SSE_data/sse_answer_posts.csv'
# column_name_for_user_id='OwnerUserId'
# count_type='answer_posts'
# text_column_name='Body'
# print('==========================================================================================')
# data4=stimpl.get_include_code_count_user_wise(file_path_for_answer_posts, column_name_for_user_id,text_column_name)
# print('**********************************   START   *******************************************')
# stimpl.cluster_data('code_count_in_answer_posts',data4)
# print('**********************************   END   *******************************************')
#
#
# file_path_for_answer_posts='C:/Users/pc/Desktop/FYP data/SSE_data/sse_question_posts.csv'
# column_name_for_user_id='OwnerUserId'
# text_column_name='Tags'
# print('==========================================================================================')
# tags=tec_skills.get_tags_user_wise(file_path_for_answer_posts, column_name_for_user_id,text_column_name)
# print('**********************************   START   *******************************************')
# stimpl.cluster_data('tags',tags)
# print('**********************************   END   *******************************************')


# file_path_for_comments='C:/Users/pc/Desktop/FYP data/SSE_data/sse_answer_posts.csv'
# column_name_for_user_id='OwnerUserId'
# text='Ensures that code artifacts produced are of the highest quali, conforming to set or agreed upon standard.'
# text+='Follows the processes, agile practices and motivates his/her team members to do So'
# text+='Escalates and communicates issues, risks and concerns to leads or managers.'
# text+='Provides input on estimates and achieve on-time Delivery,'
# text+='Aligns self to organizational goals.'
# text+='Acoepis project delivery responsibilities and demonstrate accountability to leadership.'
# text+='Maintains a sense of individuality in thinking and decision making'

# data=tpmodeling.get_topic_user_wise(file_path_for_comments,column_name_for_user_id,text)
# print('==========================================================================================',data)
# print('**********************************   START   *******************************************')
# stimpl.cluster_data('releventness_to_jobadd',data)
# print('**********************************   END   *******************************************')

#
# file_path_for_answer_posts='C:/Users/pc/Desktop/FYP data/SSE_data/sse_question_posts.csv'
# column_name_for_user_id='OwnerUserId'
# print('==========================================================================================')
# data6=stimpl.post_similarity(file_path_for_answer_posts, column_name_for_user_id)
# print('**********************************   START   *******************************************')
# stimpl.cluster_data('question_posts_similarity',data6)
# print('**********************************   END   *******************************************')



# file_path_for_answer_posts='C:/Users/pc/Desktop/FYP data/SSE_data/sse_answer_posts.csv'
# column_name_for_user_id='OwnerUserId'
# print('==========================================================================================')
# data5=stimpl.post_similarity(file_path_for_answer_posts, column_name_for_user_id)
# print('**********************************   START   *******************************************')
# stimpl.cluster_data('answer_posts_similarity',data5)
# print('**********************************   END   *******************************************')


# file_path_for_answer_posts='C:/Users/pc/Desktop/FYP data/SSE_data/sse_answer_posts.csv'
# column_name_for_user_id='OwnerUserId'
# count_type='answer_posts'
# text_column_name='CommentCount'
# print('==========================================================================================')
# data2=stimpl.get_avg_score_user_wise(file_path_for_answer_posts, column_name_for_user_id,count_type,text_column_name)
# print('**********************************   START   *******************************************')
# stimpl.cluster_data('avg_comment_count_answer_posts',data2)
# print('**********************************   END   *******************************************')


# file_path_for_answer_posts='C:/Users/pc/Desktop/FYP data/SSE_data/sse_question_posts.csv'
# column_name_for_user_id='OwnerUserId'
# count_type='answer_posts'
# text_column_name='AnswerCount'
# print('==========================================================================================')
# data2=stimpl.get_avg_score_user_wise(file_path_for_answer_posts, column_name_for_user_id,count_type,text_column_name)
# print('**********************************   START   *******************************************')
# stimpl.cluster_data('avg_answer_count_answer_posts',data2)
# print('**********************************   END   *******************************************')

# file_path_for_answer_posts='C:/Users/pc/Desktop/FYP data/SSE_data/sse_answer_posts.csv'
# column_name_for_user_id='OwnerUserId'
# count_type='answer_posts'
# text_column_name='ViewCount'
# print('==========================================================================================')
# data2=stimpl.get_avg_score_user_wise(file_path_for_answer_posts, column_name_for_user_id,count_type,text_column_name)
# print('**********************************   START   *******************************************')
# stimpl.cluster_data('avg_viewcount_count_question_posts',data2)
# print('**********************************   END   *******************************************')

# file_path_for_answer_posts='C:/Users/pc/Desktop/FYP data/SSE_data/sse_question_posts.csv'
# column_name_for_user_id='OwnerUserId'
# count_type='answer_posts'
# text_column_name='ViewCount'
# print('==========================================================================================')
# data2=stimpl.get_avg_score_user_wise(file_path_for_answer_posts, column_name_for_user_id,count_type,text_column_name)
# print('**********************************   START   *******************************************')
# stimpl.cluster_data('avg_viewcount_count_question_posts',data2)
# print('**********************************   END   *******************************************')


def get_tp_score(ntext):
    file_path_for_comments = 'C:/Users/pc/Desktop/FYP data/SE_data/se_answer_posts.csv'
    column_name_for_user_id = 'OwnerUserId'
    text = 'Ensures that code artifacts produced are of the highest quali, conforming to set or agreed upon standard.'
    text += 'Follows the processes, agile practices and motivates his/her team members to do So'
    text += 'Escalates and communicates issues, risks and concerns to leads or managers.'
    text += 'Provides input on estimates and achieve on-time Delivery,'
    text += 'Aligns self to organizational goals.'
    text += 'Acoepis project delivery responsibilities and demonstrate accountability to leadership.'
    text += 'Maintains a sense of individuality in thinking and decision making'

    data = tpmodeling.get_topic_user_wise(file_path_for_comments, column_name_for_user_id, ntext)
    stimpl.cluster_data('releventness_to_jobadd', data)