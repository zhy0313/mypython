#! /usr/bin/python
 # -*- coding: utf-8 -*- 

import os,sys
import cx_Oracle,pysvn
import time
import re
import subprocess
import shutil,pickle
import Dispatcher_Check

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.ZHS16GBK'

def printRedInfo(strInfo):
    print("\n\033[0;1;31;5m%s\033[0m\n" % strInfo)

def generate_deploy_script(targetfile,serverinfoid,job_info,var_dict,style):    
    line1 = r"@echo %s" % ("="*100)
    line2 = r"@echo %s : ·t???÷: %s  ó??§: %s" % (serverinfoid,var_dict['IP'],var_dict['User'])    
    line3 = "@call ant -buildfile "+job_info['local_dir']+r"\build.xml" +" -Dhost="+var_dict['IP']\
            +" -Duser="+var_dict['User']+" -Dpassword="+var_dict['Password']+" -DrootPath="+var_dict['Appdir']\
            +" -Ddeploy="+var_dict['Package']+" -DbakSh="+var_dict['Backpath']+" -DstopSh="+var_dict['Stoppath']\
            +" -DstartSh="+var_dict['Startpath']+" -DstopScript="+var_dict['Checkstoppath']\
            +" -DdelBakScript="+var_dict['Delbackpath']+" -DdelHupScript="+var_dict['Delnohuppath']\
            +" -DcopyProgramPath="+var_dict['Checklistpath']+" -DcopyFileScript="+var_dict['Copypath']\
            +" -DJOBDIR="+job_info['job_dir']+" -DdelCache="+var_dict['delCache']+" -Dbak="+var_dict['Bak']
    if style!='':
        line3 = line3+" -Dstyle="+style
    fw_deploy = open(targetfile,'w')
    fw_deploy.writelines(line1+"\n")
    fw_deploy.writelines(line2+"\n")
    fw_deploy.writelines(line3+"\n")
    fw_deploy.writelines(line1+"\n")
    fw_deploy.close()

def generate_sql_exec_script(targetfile,serverinfoid,job_info,var_dict,style,Svnpath,operate):
    #±è??SQL×??ˉ?ˉ×??üá?′?μ?SVNμ??·
    today = time.strftime('%Y%m%d',time.localtime(time.time()))
    svn_changed=False
    if style.find(r'SQL')!=-1 and re.search(r'_%s_'%'VIR|PRD|PRO',operate):
        svn_file_path = r'%s\release\svnAddr.ini' % job_info['job_dir']
        if not os.path.exists(svn_file_path):
            #print("???t2?′??ú?aê?′′?¨")
            fw = open(svn_file_path,'wb')
            pickle.dump(today,fw)
            pickle.dump(Svnpath,fw)
            fw.close()
        fr = open(svn_file_path,'rb')
        last_date=pickle.load(fr)
        last_svnAddr=pickle.load(fr)
        #print("é?′?ê±??￡o",last_date)
        #print("é?′?SVNμ??·￡o",last_svnAddr)
        #print("±?′?SVNμ??·",Svnpath)
        fr.close()
        if today==last_date and Svnpath!=last_svnAddr:
            svn_changed=True
            #print("SVNμ??·óD±??ˉ")
        fw = open(svn_file_path,'wb')
        pickle.dump(today,fw)
        pickle.dump(Svnpath,fw)
        fw.close()
    else:
        pass

    line1 = r"@echo %s" % ("="*100)
    line2 = r"@echo %s : ·t???÷: %s  ó??§: %s" % (serverinfoid,var_dict['IP'],var_dict['User'])
    if svn_changed:
        line3 = "@call ant -buildfile "+job_info['local_dir']+r"\build-sql.xml" +" -Dhost="+var_dict['IP']\
            +" -Duser="+var_dict['User']+" -Dpassword="+var_dict['Password']+" -DrootPath="+var_dict['Appdir']\
            +" -Ddeploy="+var_dict['Package']+" -DstopSh="+var_dict['Stoppath']\
            +" -DstartSh="+var_dict['Startpath']+" -DJOBDIR="+job_info['job_dir']\
            +" -DsvnAddrChangedTag=yes"
    else:
        line3 = "@call ant -buildfile "+job_info['local_dir']+r"\build-sql.xml" +" -Dhost="+var_dict['IP']\
            +" -Duser="+var_dict['User']+" -Dpassword="+var_dict['Password']+" -DrootPath="+var_dict['Appdir']\
            +" -Ddeploy="+var_dict['Package']+" -DstopSh="+var_dict['Stoppath']\
            +" -DstartSh="+var_dict['Startpath']+" -DJOBDIR="+job_info['job_dir']\
            +" -DsvnAddrChangedTag=no"
    if style!='':
        line3 = line3+" -Dstyle="+style
    fw_deploy = open(targetfile,'w')
    fw_deploy.writelines(line1+"\n")
    fw_deploy.writelines(line2+"\n")
    fw_deploy.writelines(line3+"\n")
    fw_deploy.writelines(line1+"\n")
    fw_deploy.close()

def generate_test_script(targetfile,serverinfoid,job_info,var_dict,style):    
    line1 = r"@echo %s" % ("="*100)
    line2 = r"@echo %s : ·t???÷: %s  ó??§: %s" % (serverinfoid,var_dict['IP'],var_dict['User'])
    line5 = "@call ant -buildfile "+job_info['local_dir']+r"\build-testing.xml"+" -Dhost="+var_dict['IP']\
            +" -Duser="+var_dict['User']+" -Dpassword="+var_dict['Password']+" -DtestingSh="+var_dict['Checkstartpath']\
            +" -DcopyProgramPath="+var_dict['Checklistpath']+" -DcopyFileScript="+var_dict['Copypath']\
            +" -DJOBDIR="+job_info['job_dir']
    if style!='':
        line5 = line5+" -Dstyle="+style
    fw_testing = open(targetfile,'w')
    fw_testing.writelines(line1+"\n")
    fw_testing.writelines(line2+"\n")
    fw_testing.writelines(line5+"\n")
    fw_testing.writelines(line1+"\n")
    fw_testing.close()

def generate_svn_script(targetfile,db_info,job_info,style,operate):
    today = time.strftime('%Y%m%d',time.localtime(time.time()))
    conn = cx_Oracle.connect(db_info)
    cursor = conn.cursor()    
    svn_info = cursor.execute(job_info['svn_info_sql'].replace('*','svndir,svnusername,svnpass')).fetchall()
    Svnpath = svn_info[0][0].strip()
    
    try:
        client = pysvn.Client()
        #client.list(Svnpath)
    except:
        printRedInfo("???ì2é????1üàí??ì¨SVNμ??·μ??yè·D?￡?￡?")
        sys.exit(0)
    
    Svnuser = svn_info[0][1].strip()
    Svnpassword = svn_info[0][2].strip()
    if re.search(r'_SQLRELEASE$',operate):
        dest_name=r'program\SQL'
    else:
        dest_name=r'program\3ìDò'
    line20 = r"@echo svnant.this.url= %s> %s\release\%s\script\svn.properties" %(Svnpath,job_info['job_dir'],style+today)
    line21 = r"@echo svnant.repository.user= %s>> %s\release\%s\script\svn.properties" % (Svnuser,job_info['job_dir'],style+today)
    line22 = r"@echo svnant.repository.passwd= %s>> %s\release\%s\script\svn.properties" % (Svnpassword,job_info['job_dir'],style+today)
    line23 = r"@call ant -buildfile  %s\build-svn.xml -DJOBDIR=%s -Ddest_name=%s" % (job_info['local_dir'],job_info['job_dir'],dest_name)
    if style!='':
        line23 = line23+" -Dstyle="+style
    line_list = [line20,line21,line22,line23]
    fw_svn = open(targetfile,'w')
    for line in line_list:
        fw_svn.writelines(line+'\n')
    fw_svn.close()
    
def generate_switch_property(targetfile,db_info,job_info):
    conn = cx_Oracle.connect(db_info)
    cursor = conn.cursor()
    var_attr_relation_dict = dict(switch_scp='switch_scp',switch_bak='switch_bak',
                                  switch_stop='switch_stop',switch_start='switch_start',
                                  switch_delnohup='switch_delnohup',switch_delbak='switch_delbak',
                                  switch_checkfile='switch_checkfile',switch_delcache='switch_delcache')
    switch_dict = {}
    for var_key,var_value in var_attr_relation_dict.items():
        temp_flag = cursor.execute(job_info['svn_info_sql'].replace('*',var_value)).fetchall()[0][0]
        if temp_flag==1:
            switch_dict[var_key] = 'true'
        else:
            switch_dict[var_key] = 'false'
    #μ￥?à′|àíswitch_system×???,0ê?linux￡?1ê?windows2003,2ê?windows2008
    temp_flag_2 = cursor.execute(job_info['svn_info_sql'].replace('*','switch_system')).fetchall()[0][0]
    if temp_flag_2==1:
        switch_dict['switch_system'] = '2003'
    elif temp_flag_2==2:
        switch_dict['switch_system'] = '2008'
    else:
        pass
    line30 = r'switch-scp = %s' % switch_dict['switch_scp']
    line31 = r'switch-bak = %s' % switch_dict['switch_bak']
    line32 = r'switch-stop = %s' % switch_dict['switch_stop']
    line33 = r'switch-start = %s' % switch_dict['switch_start']
    line34 = r'switch-delNohup = %s' % switch_dict['switch_delnohup']
    line35 = r'switch-delBak = %s' % switch_dict['switch_delbak']
    line36 = r'switch-checkFile = %s' % switch_dict['switch_checkfile']
    line37 = r'switch-delCache = %s' % switch_dict['switch_delcache']
    line_list = [line30,line31,line32,line33,line34,line35,line36,line37]
    #?D??è?1?ê?windows?μí3￡?2?éú3éswitch_system×???
    if 'switch_system' in switch_dict:
        line38 = r'switch-system = %s' % switch_dict['switch_system']
        line_list.append(line38)
    fw_switch = open(targetfile,'w')
    for line in line_list:
        fw_switch.writelines(line+'\n')
    fw_switch.close()

def generate_getfilelist_script(targetfile,job_info):    
    line40 = r'@echo off &setlocal enabledelayedexpansion '
    line41 = r'set today=%date:~0,4%%date:~5,2%%date:~8,2%'
    line42 = r'set rootdir=%s'%job_info['job_dir']
    line43 = r'set rootdir1=%rootdir%\release\3ìDò_%today%\program\3ìDò'
    line44 = r'cd /d %rootdir1%'
    line45 = r'dir .\*.* /s/b/a:-d > ..\..\script\list%today%.txt'
    line46 = r'set f=%rootdir%\release\3ìDò_%today%\script\list%today%.txt'
    line47 = r'set f3=%rootdir%\release\3ìDò_%today%\script\list_new.txt'
    line48 = 'set flag1=0\nset flag2=0\nset flag3=0'
    line49 = r'@rem --------------------???t?·??ì???-----------------------'
    line50 = r'if exist %f3%  (del /q %f3%)  '
    line51 = r'for /f "tokens=* delims=" %%l in (%f%) do ( '
    line52 = r'set /a flag1=flag1+1'
    line53 = r'set var=%%l'
    line54 = r'set var=!var:%rootdir%\release\3ìDò_%today%\program\3ìDò\=! '
    line55 = r'set var=!var:\=/!'
    line56 = r'set var=!var: =!'
    line57 = r'echo !var!>>%f3%'
    line58 = r')'
    line_list = [line40,line41,line42,line43,line44,line45,line46,line47,line48,line49,\
                 line50,line51,line52,line53,line54,line55,line56,line57,line58]
    fw_gfl = open(targetfile,'w')
    for line in line_list:
        fw_gfl.writelines(line+'\n')
    fw_gfl.close()

def generate_rollback_script(targetfile,serverinfoid,job_info,var_dict):
    line60 = r"@echo %s" % ("="*100)
    line61 = r"@echo %s : ·t???÷: %s  ó??§: %s" % (serverinfoid,var_dict['IP'],var_dict['User'])
    line2 = "@call ant -buildfile "+job_info['job_dir']+r"\script\build-rollback.xml" +" -Dhost="+var_dict['IP']\
            +" -Duser="+var_dict['User']+" -Dpassword="+var_dict['Password']+" -DrootPath="+var_dict['Appdir']\
            +" -Ddeploy="+var_dict['Package']+" -DrollbackSh="+var_dict['Rollbackpath']
    fw_deploy = open(targetfile,'w')
    fw_deploy.writelines(line1+"\n")
    fw_deploy.writelines(line2+"\n")
    fw_deploy.writelines(line3+"\n")
    fw_deploy.writelines(line1+"\n")
    fw_deploy.close()
    
def make_directory(job_dir,operate):
    today = time.strftime('%Y%m%d',time.localtime(time.time()))    
    if re.search(r'_%s$'%'RELEASE',operate):
        cx_todaydir = r"%s\release\3ìDò_%s"%(job_dir,today)
        if(os.path.exists(cx_todaydir)):
            modify_time = time.strftime('%Y%m%d_%H%M%S', time.localtime(os.path.getmtime(cx_todaydir)))
            new_name = os.path.dirname(cx_todaydir)+os.sep+'3ìDò_'+str(modify_time)
            os.rename(cx_todaydir,new_name)
        os.makedirs(cx_todaydir+os.sep+"script")
        os.makedirs(cx_todaydir+os.sep+"log")
        os.makedirs(cx_todaydir+os.sep+"program")
        os.makedirs(cx_todaydir+os.sep+"program"+os.sep+"3ìDò")
    elif re.search(r'_%s$'%'SQLRELEASE',operate):
        sql_todaydir = r"%s\release\SQL_%s"%(job_dir,today)
        if(os.path.exists(sql_todaydir)):
            modify_time = time.strftime('%Y%m%d_%H%M%S', time.localtime(os.path.getmtime(sql_todaydir)))
            new_name = os.path.dirname(sql_todaydir)+os.sep+'SQL_'+str(modify_time)
            os.rename(sql_todaydir,new_name)
        os.makedirs(sql_todaydir+os.sep+"script")
        os.makedirs(sql_todaydir+os.sep+"program")
        os.makedirs(sql_todaydir+os.sep+"program"+os.sep+"SQL")
    else:
        todaydir = r"%s\release\%s"%(job_dir,today)
        if(os.path.exists(todaydir)):
            modify_time = time.strftime('%Y%m%d_%H%M%S', time.localtime(os.path.getmtime(todaydir)))
            new_name = os.path.dirname(todaydir)+os.sep+str(modify_time)
            os.rename(todaydir,new_name)
        os.makedirs(todaydir+os.sep+"script")
    #if not (os.path.exists(todaydir)):
    #    os.makedirs(job_dir+os.sep+"rollback")


def dispatcher(db_info,job_info,operate):
    today = time.strftime('%Y%m%d',time.localtime(time.time()))
    if re.search(r'_%s$'%'RELEASE',operate):
        style = r'3ìDò_'
    elif re.search(r'_%s$'%'SQLRELEASE',operate):
        style = r'SQL_'
    else:
        style = r''
    getfilelist_targetfile = r'%s\getFileList.bat'%job_info['job_dir']
    switch_targetfile = r'%s\global.properties'%job_info['job_dir']
    svn_targetfile = r'%s\release\%s\script\svn_%s.bat'%(job_info['job_dir'],style+today,today)
    generate_getfilelist_script(getfilelist_targetfile,job_info)    
    generate_switch_property(switch_targetfile,db_info,job_info)

    conn = cx_Oracle.connect(db_info)
    cursor = conn.cursor()
    switch_scp = cursor.execute(job_info['svn_info_sql'].replace('*','switch_scp')).fetchall()[0][0]
    if re.search(r'_%s_'%('VIR|PRD|PRO'),operate) and re.search(r'_%s$'%'SQLRELEASE',operate):
        svn_info = cursor.execute(job_info['svn_info_sql'].replace('*','svndir,svnusername,svnpass')).fetchall()
        Svnpath = svn_info[0][0].strip()
        #print("Svnpath=",Svnpath)
    if switch_scp==1:
        if re.search(r'_%s_'%'VIR|PRD|PRO',operate):
            generate_svn_script(svn_targetfile,db_info,job_info,style,operate)
            svn_pipe = subprocess.Popen(svn_targetfile,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
            stdoutdata,stderrdata=svn_pipe.communicate()
            print(stdoutdata)
            print(stderrdata)
        else:
            srcdir = r'%s\BUILD\release\%s\program\%s'%(os.path.dirname(job_info['job_dir']),today,re.sub('_','',style))
            dstdir = r'%s\release\%s\program\%s'%(job_info['job_dir'],style+today,re.sub('_','',style))
            if os.path.exists(dstdir):
                shutil.rmtree(dstdir)
            if os.path.exists(srcdir):
                shutil.copytree(srcdir,dstdir)
            else:
                print('BUILD???????ò2?μ???ììμ?±àò??á1?°ü￡???o???!!')
                sys.exit()
    #?D??program\3ìDò????′??ú2￠?ò2??a??￡??òDèòaéú3é3ìDò??μ￥
    program_dir = r'%s\release\%s\program\3ìDò'%(job_info['job_dir'],style+today)
    if os.path.exists(program_dir) and len(os.listdir(program_dir))!=0:
        svn_pipe = subprocess.Popen(getfilelist_targetfile,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
        stdoutdata,stderrdata=svn_pipe.communicate()
        print(stdoutdata)
        print(stderrdata)

    records = cursor.execute(job_info['server_info_sql'].replace('*','menuid,serverinfoid')+" ORDER BY serverinfoid").fetchall()
    if len(records)<=20:
        records_group = [ records[0:(len(records)//2)] ,records[(len(records)//2):] ]
    else:
        item = len(records)//10
        records_group = []
        for i in range(1,item):
            records_group.append(records[10*(i-1):10*i]) 
        records_group.append(records[10*item:])

    var_attr_relation_dict = dict(IP='ip',Port='port',User='servername',\
                Password='serverpassword',Appdir='appdir',Package='appname',\
                Backpath='bacdir',Stoppath='stopdir',\
                Startpath='startdir',Checkstartpath='checkstart',\
                Checkstoppath='checkstop',Delbackpath='delbac',\
                Delnohuppath='dellog',Checklistpath='checkuploaddir',\
                Copypath='copydir',delCache='delcache',Bak='bak')#,Rollbackpath='rollbackdir'
    var_dict = {}
    for group in records_group:
        pipes = []
        if len(group)>0:
            for record in group:
                var_dict.clear()
                for var_key,var_value in var_attr_relation_dict.items():
                    sql_cmd = job_info['server_info_sql'].replace('*',var_value)+(" and serverinfoid='%s'"%record[1])
                    var_dict[var_key] = cursor.execute(sql_cmd).fetchall()[0][0]       
                deploy_targetfile = r'%s\release\%s\script\deploy_%s_%s.bat'%(job_info['job_dir'],style+today,var_dict['IP'],var_dict['Port'])
                testing_targetfile = r'%s\release\%s\script\testing_%s_%s.bat'%(job_info['job_dir'],style+today,var_dict['IP'],var_dict['Port'])            
                generate_deploy_script(deploy_targetfile,record[1],job_info,var_dict,style)
                generate_test_script(testing_targetfile,record[1],job_info,var_dict,style)
                switch_bak = cursor.execute(job_info['svn_info_sql'].replace('*','switch_bak')).fetchall()[0][0]
                if switch_bak==1:
                    deploy_cmd = deploy_targetfile
                elif switch_scp==1 and re.search(r'_%s$'%'SQLRELEASE',operate):
                    sql_exec_targetfile = r'%s\release\%s\script\sql_exec_%s_%s.bat'%(job_info['job_dir'],style+today,var_dict['IP'],var_dict['Port'])
                    if re.search(r'%s_%s$'%('UAT|DAT|DEV','SQLRELEASE'),operate):
                        Svnpath=r''
                    generate_sql_exec_script(sql_exec_targetfile,record[1],job_info,var_dict,style,Svnpath,operate)
                    deploy_cmd = sql_exec_targetfile
                #elif switch_rollback==1:
                #   rollback_targetfile = r'%s\rollback\%s\rollback_%s_%s.bat'%(job_info['job_dir'],today,var_dict['IP'],var_dict['Port'])
                #   generate_rollback_script(deploy_targetfile,record[1],job_info,var_dict)
                #   deploy_cmd = '%s && %s'%(rollback_targetfile,testing_targetfile)
                else:
                    deploy_cmd = '%s && %s'%(deploy_targetfile,testing_targetfile)
                pipe = subprocess.Popen(deploy_cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
                pipes.append(pipe)
            print('%s %s processes running!%s'%('$'*20,len(pipes),'$'*20))
            for pipe in pipes:#?3Dòê?3??÷ì¨·t???÷μ??′DD?é??
                stdoutdata,stderrdata=pipe.communicate()
                print(stdoutdata)
                print(stderrdata)
        else:
            pass

def get_job_info(db_info,operate):
    job_info_sql = "SELECT parentid,jobdir FROM PF_MENU WHERE name='%s'" % operate
    conn = cx_Oracle.connect(db_info)
    cursor = conn.cursor()
    info_list = cursor.execute(job_info_sql).fetchone()    
    job_id = info_list[0]
    job_dir = re.sub(r'\\\\',r'\\',info_list[1])
    operateflag_dict = {'BACKUP':'bakflag','RELEASE':'releaseflag','RESTART':'restartflag','ROLLBACK':'rollbackflag','SQLRELEASE':'sqlflag'}
    for key,value in operateflag_dict.items():
        if re.search(r'_%s$'%key,operate):
            operateflag = value
            break    
    server_info_sql = "SELECT * FROM PF_SERVERINFO WHERE menuid='%s' and %s='1'"%(job_id,operateflag)
    svn_info_sql = "SELECT * FROM PF_MENU where name='%s'"%operate
    local_dir = os.path.dirname(__file__)#r'D:\jenkins_linux_script'#
    job_info = dict(local_dir=local_dir,job_dir=job_dir,server_info_sql=server_info_sql,svn_info_sql=svn_info_sql)
    cursor.close()
    conn.close()
    return job_info    

if __name__=="__main__":
    time1 = time.time()
    cf = open(os.path.dirname(__file__)+"/settings.conf",'r')#?áè?????D??￠
    db_info = re.findall('db_info=.*',cf.read())[0].replace('db_info=','')#'abscm/abscm@10.10.142.100/configinfo'
    operate = sys.argv[1]#'21DANZHENG_DAT_SQLRELEASE'#
    conn = cx_Oracle.connect(db_info)
    cursor = conn.cursor()
    if re.search(r'_%s$'%'CHECK',operate):
        job_info = Dispatcher_Check.get_job_info(db_info,operate)    
        Dispatcher_Check.make_directory(job_info['job_dir'])
        Dispatcher_Check.dispatcher(db_info,job_info)
    else:
        job_info = get_job_info(db_info,operate)
        make_directory(job_info['job_dir'],operate)
        dispatcher(db_info,job_info,operate)
    time2 = time.time()
    print('total time:%f s'%(time2-time1))










        

    
