from django.conf.urls import url
from faconstor.views import *
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^favicon.ico$', RedirectView.as_view(url=r'static/new/images/favicon.ico')),
    url(r'^$', index, {'funid': '2'}),
    url(r'^test/$', test),
    url(r'^processindex/(\d+)/$', processindex),
    url(r'^index/$', index, {'funid': '2'}),
    url(r'^get_process_rto/$', get_process_rto),
    url(r'^get_daily_processrun/$', get_daily_processrun),
    url(r'^get_process_index_data/$', get_process_index_data),
    url(r'^monitor/$', monitor),
    url(r'^get_monitor_data/$', get_monitor_data),
    url(r'^get_clients_status/$', get_clients_status),

    # 用户登录
    url(r'^login/$', login),
    url(r'^userlogin/$', userlogin),
    url(r'^forgetPassword/$', forgetPassword),
    url(r'^resetpassword/([0-9a-zA-Z]{8}-[0-9a-zA-Z]{4}-[0-9a-zA-Z]{4}-[0-9a-zA-Z]{4}-[0-9a-zA-Z]{12})/$',
        resetpassword),
    url(r'^reset/$', reset),
    url(r'^password/$', password),
    url(r'^userpassword/$', userpassword),

    # 系统维护
    url(r'^organization/$', organization, {'funid': '61'}),
    url(r'^orgdel/$', orgdel),
    url(r'^orgmove/$', orgmove),
    url(r'^orgpassword/$', orgpassword),
    url(r'^group/$', group, {'funid': '62'}),
    url(r'^groupsave/$', groupsave),
    url(r'^groupdel/$', groupdel),
    url(r'^getusertree/$', getusertree),
    url(r'^groupsaveusertree/$', groupsaveusertree),
    url(r'^getfuntree/$', getfuntree),
    url(r'^groupsavefuntree/$', groupsavefuntree),
    url(r'^function/$', function, {'funid': '63'}),
    url(r'^fundel/$', fundel),
    url(r'^funmove/$', funmove),

    # 客户端管理
    url(r'^target/$', target, {'funid': '71'}),
    url(r'^target_data/$', target_data),
    url(r'^target_save/$', target_save),
    url(r'^target_del/$', target_del),

    url(r'^origin/$', origin, {'funid': '70'}),
    url(r'^origin_data/$', origin_data),
    url(r'^origin_save/$', origin_save),
    url(r'^origin_del/$', origin_del),

    # 主机管理
    url(r'^hosts_manage/$', hosts_manage, {'funid': '68'}),
    url(r'^host_save/$', host_save),
    url(r'^hosts_manage_data/$', hosts_manage_data),
    url(r'^hosts_manage_del/$', hosts_manage_del),

    # 预案管理
    url(r'^script/$', script, {'funid': '32'}),
    url(r'^scriptdata/$', scriptdata),
    url(r'^scriptdel/$', scriptdel),
    url(r'^scriptsave/$', scriptsave),
    url(r'^scriptexport/$', scriptexport),
    url(r'^processconfig/$', processconfig, {'funid': '31'}),
    url(r'^processscriptsave/$', processscriptsave),
    url(r'^get_script_data/$', get_script_data),
    url(r'^remove_script/$', remove_script),
    url(r'^setpsave/$', setpsave),
    url(r'^custom_step_tree/$', custom_step_tree),
    url(r'^processconfig/$', processconfig, {'funid': '63'}),
    url(r'^del_step/$', del_step),
    url(r'^move_step/$', move_step),
    url(r'^get_all_groups/$', get_all_groups),
    url(r'^processdesign/$', process_design, {"funid": "33"}),
    url(r'^process_data/$', process_data),
    url(r'^process_save/$', process_save),
    url(r'^process_del/$', process_del),
    url(r'^verify_items_save/$', verify_items_save),
    url(r'^get_verify_items_data/$', get_verify_items_data),
    url(r'^remove_verify_item/$', remove_verify_item),

    # Oracle恢复
    url(r'^oracle_restore/(?P<process_id>\d+)$', oracle_restore),
    url(r'^oracle_restore_data/$', oracle_restore_data),
    url(r'^cv_oracle_run/$', cv_oracle_run),
    url(r'^cv_oracle/(\d+)/$', cv_oracle, {'funid': '49'}),
    url(r'^save_invitation/$', save_invitation),
    url(r'^cv_oracle_run_invited/$', cv_oracle_run_invited),
    url(r'^fill_with_invitation/$', fill_with_invitation),
    url(r'^save_modify_invitation/$', save_modify_invitation),

    url(r'^getrunsetps/$', getrunsetps),
    url(r'^cv_oracle_continue/$', cv_oracle_continue),
    url(r'^processsignsave/$', processsignsave),
    url(r'^get_current_scriptinfo/$', get_current_scriptinfo),
    url(r'^ignore_current_script/$', ignore_current_script),
    url(r'^stop_current_process/$', stop_current_process),
    url(r'^verify_items/$', verify_items),
    url(r'^show_result/$', show_result),
    url(r'^reject_invited/$', reject_invited),
    url(r'^reload_task_nums/$', reload_task_nums),
    url(r'^delete_current_process_run/$', delete_current_process_run),
    url(r'^get_celery_tasks_info/$', get_celery_tasks_info),
    url(r'^revoke_current_task/$', revoke_current_task),
    url(r'^get_script_log/$', get_script_log),
    url(r'^save_task_remark/$', save_task_remark),
    url(r'^get_server_time_very_second/$', get_server_time_very_second),

    url(r'^get_force_script_info/$', get_force_script_info),


    # 历史查询
    url(r'^custom_pdf_report/$', custom_pdf_report),
    url(r'^restore_search/$', restore_search, {'funid': '64'}),
    url(r'^restore_search_data/$', restore_search_data),
    url(r'^tasksearch/$', tasksearch, {'funid': '65'}),
    url(r'^tasksearchdata/$', tasksearchdata),

    # 其他
    url(r'^downloadlist/$', downloadlist, {'funid': '7'}),
    url(r'^download/$', download),
    url(r'^download_list_data/$', download_list_data),
    url(r'^knowledge_file_del/$', knowledge_file_del),

    # 邀请
    url(r'^invite/$', invite),
    url(r'^get_all_users/$', get_all_users),

    # 通讯录
    url(r'^contact/$', contact, {'funid': '67'}),
    url(r'^get_contact_tree/$', get_contact_tree),
    url(r'^get_contact_info/$', get_contact_info),

    # 服务器信息配置
    url(r'^serverconfig/$', serverconfig, {'funid': '72'}),
    url(r'^serverconfigsave/$', serverconfigsave),

    # 备份内容
    url(r'^backup_content/$', backup_content, {'funid': '74'}),
    url(r'^get_backup_content/$', get_backup_content),

    # 计划策略
    url(r'^schedule_policy/$', schedule_policy, {'funid': '75'}),
    url(r'^get_schedule_policy/$', get_schedule_policy),

    # 存储策略
    url(r'^storage_policy/$', storage_policy, {'funid': '76'}),
    url(r'^get_storage_policy/$', get_storage_policy),

    # 备份状态
    url(r'^backup_status/$', backup_status, {'funid': '78'}),
    url(r'^get_backup_status/$', get_backup_status),

    # 自主恢复
    url(r'^manualrecovery/$', manualrecovery, {'funid': '79'}),
    url(r'^manualrecoverydata/$', manualrecoverydata),

    url(r'^dooraclerecovery/$', dooraclerecovery),
    url(r'^oraclerecoverydata/$', oraclerecoverydata),

    # 演练概况
    url(r'^get_process_run_facts/$', get_process_run_facts),

    # 流程计划
    url(r'^process_schedule/$', process_schedule, {'funid': '84'}),
    url(r'^process_schedule_save/$', process_schedule_save),
    url(r'^process_schedule_data/$', process_schedule_data),
    url(r'^change_periodictask/$', change_periodictask),
    url(r'^process_schedule_del/$', process_schedule_del),

    url(r'^phyproconfig/$', phyproconfig, {'funid': '87'}),
    url(r'^phyproconfigdata/$', phyproconfigdata),
    url(r'^getphydataget/$', getphydataget),
    url(r'^phyproconfigsaveapp/$', phyproconfigsaveapp),
    url(r'^phyproconfigsavefile/$', phyproconfigsavefile),
    url(r'^phyproconfigsaveoracle/$', phyproconfigsaveoracle),
    url(r'^phyproconfigsavemssql/$', phyproconfigsavemssql),


    url(r'^vmproconfig/$', vmproconfig, {'funid': '88'}),
    url(r'^vmproconfigdata/$', vmproconfigdata),
    url(r'^vmproconfigsave/$', vmproconfigsave),
    url(r'^getvmlist/$', getvmlist),
    url(r'^vmappsave/$', vmappsave),
    url(r'^vmproconfigdel/$', vmproconfigdel),
    url(r'^vmappdel/$', vmappdel),

    url(r'^resourcepool/$', resourcepool, {'funid': '90'}),
    url(r'^resourcepooldata/$', resourcepooldata),
    url(r'^resourcepoolsave/$', resourcepoolsave),
    url(r'^resourcepooldel/$', resourcepooldel),
    url(r'^getvendorlist/$', getvendorlist),

    url(r'^backupresource/$', backupresource, {'funid': '91'}),
    url(r'^backupresourcedata/$', backupresourcedata),
    url(r'^backupresourcepooldata/$', backupresourcepooldata),
    url(r'^backupresourcesave/$', backupresourcesave),
    url(r'^backupresourcedel/$', backupresourcedel),
    url(r'^getbackupcert/$', getbackupcert),

    url(r'^schduleresource/$', schduleresource, {'funid': '92'}),
    url(r'^schduleresourcedata/$', schduleresourcedata),
    url(r'^schduleresourcepooldata/$', schduleresourcepooldata),
    url(r'^schduleresourcesave/$', schduleresourcesave),
    url(r'^schduleresourcedel/$', schduleresourcedel),
    url(r'^getschdulecert/$', getschdulecert),

    url(r'^oraclerecovery/(\d+)/$', oraclerecovery),
    url(r'^dooraclerecovery/$', dooraclerecovery),
    url(r'^oraclerecoverydata/$', oraclerecoverydata),

    url(r'^mssqlrecovery/(\d+)/$', mssqlrecovery),
    url(r'^domssqlrecovery/$', domssqlrecovery),
    url(r'^mssqlrecoverydata/$', mssqlrecoverydata),

    url(r'^filerecovery/(\d+)/$', filerecovery),
    url(r'^dofilerecovery/$', dofilerecovery),
    url(r'^filerecoverydata/$', filerecoverydata),
    url(r'^getfiletree/$', getfiletree),

    url(r'^vmrecovery/(\d+)/$', vmrecovery),
    url(r'^getproxylist/$', getproxylist),
    url(r'^dovmrecovery/$', dovmrecovery),
    url(r'^vmrecoverydata/$', vmrecoverydata),
]
