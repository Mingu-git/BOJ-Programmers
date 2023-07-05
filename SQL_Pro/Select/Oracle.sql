"""
정리

12.09

From 연수

About Oracle , basic Gram

기본 문법

1. != == <> 

"""

1) Instr : 문자열에서 원하는 문자를 찾을 때 INSTR
시작은 1부터 시작 + int 형태로 반환
ex ) Instr('test@naver.com', '@') + 1 ==5+1 = 6


2) substr(문자열 ,st, end)  -- for 문자열을 자르기 위한 함수 --
--다음과 같이 사용됨  -- 
Select substr(naver , 1,2) , empno as 번호
from dual   

이렇게 할시 그냥  (a,empno) 쌍으로 반복해서 출력.


3) REGEXP_SUBSTR('원하는 문지열' , '정규식 패턴', 1(검색시작 위치) , 1 (패턴 일치 발생 횔수) )  -- 정규표현식 버전  오라클 10g 부터 시작--
select REGEXP_SUBSTR("abc" , '[a]+', 1, 1)

4) To_Date
Select ename , hirecate
from empno
where hirecate = To_Date(1994.12.12 , "YYYY.MM.DD")


5) Trunc  : for 소수점 절사 및 날짜와 시간을 없앨때
ex)  
Select Trunc(date)
from emp

6) Case(알잖아)

ex)
Case Deptno when 10 then 'a'
when 20 then 'c'
when 30 then 'd'
end as num
from dual



7) union = 합집합(중복제거) ,, union all = 중복행포함

8) 다중행 서브 쿼리 where sal (in,any,all ,)
In = 서브쿼리안에 값있을시 반환
all = 서브쿼리의 모든값확인후 반환
any = 하나라도 있으면 반환


"""
12.09 oracle 정리

"""

1. create 
create table book(
bno NUMBER(3),
bname varchar(10)

);


2.값추가

INSERT INTO BOOK(10,"노인의 바다")

3. update

update border
set OQTY = 5
WHERE ONO = 2;

4. alter
add 대신 moodify , drop column (컬럼) , RENAME column a to b;

alter table Border add (Odate NUMBER(5));




"""
퀴즈 3, 4 , 5 정리

"""

1. 날짜

where hirecate > '81/04/02' and hirecate < '80/01/01'


2. Like

Where Ename Like "S__T"   // _ = 한자릿수 , % = 계속 아무거나

3. TO_CHAR(hiredate ,'YYYY'년 'MM'월)

+@ SYSDATE = 현제 날짜 
ex ) select SYSDATE as date

4. 두번째로 많은 급여  == 최고급여를 제외한 테이블 생성( from 을 통해) 그후 max = 2번째 큰 값
select ename , sal
from emp
where sal = (
    select max(sal)
    from (
        select sel 
        from emp
        where sal < (select max(sal) from emp)
    )

)

5. length(name) = 5