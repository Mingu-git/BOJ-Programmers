"""
정리

1208

connect by
partition by
rank
groupconcat

sqlp

"""


Select 문제
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
1 번 : 12세 이하인 여자 환자 목록 출력하기.

POINT : SELECT IF NULL(TLN , "방구") as TLNO
POINT : ORDER BY AGE DSEC , PT_NO ASC

2: 강원도에 위치한 생산공장 목록 출력하기

POINT : WHERE ADDRES Like "강원도%"

3: 3월에 태어난 여성 회원 목록 출력하기

POINT : SELECT DATE_FORMAT(DATE_OF_BIRTH , "%Y-%m-%d") as 생일빵목록
POINT : WHERE TLNO IS not NULL

4.재구매가 일어난 상품과 회원 리스트 구하기

POINT : GROUP By User_ID , PRODUCT_ID
POINT : Having Count(*) >= 2

// GROUP By 쓸때 앞뒤에 WHERE 절 넣어서 비교 가능

DATE_FORMAT 문제
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

select DATE_FORMAT(DATE_OF_BIRTH , '%Y-%m-%d')

Sum,MAX,MIN 문제
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

1. 가장 비싼 상품 구하기

POINT : MAX(PRICE) as MAX_PRICE

2.가격이 제일 비싼 식품의 정보 출력하기

POINT : WHERE Price = (Select Max(Price) as PRICE 
                            From table)
POINT : == ORDER By Price DESC
           Limit 1;

둘이 최고가격 출력 비슷

3.최대값 구하기

POINT : Select max(datetime) as 시간 = 최근 = max

4.중복 제거하기

POINT : Select Count(Distinct(name_class)) as name_C

POINT : name_class is not NULL

ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
GROUP by

1. 진료과별 총 예약 횟수 출력하기

POINT : Select Count(*) as 건수   //APPIT컬럼의 중복의 갯수 출력
POINT :GROUP by APPIT

2.즐겨찾기가 가장 많은 식당 정보 출력

Point : where (FAVORITES,FOOD_type) in (Select Max(FAVORITES),food_type
                                        from REST_INFO
                                        Group by FOOD_TYPE)


ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
NULL

1.경기도에 위치한 식품창고 목록 출력하기

POINT : SELECT IFNULL(FREEZER_YN , 'N')

2. NULL 처리하기

Point : IFNULL( 컬럼 , 값) 컬럼 == NULL RETURN 값 ELSE A (컬럼 그자체)
NULLIF( A,B) => A==B return NULL else A

ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
IF

1. SELECT IF(A.SEQ >= 3 , 'A' , 'B') AS RESULT (3보다 크면 A, 아닐시 B)

ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

CASE

1. CASE
			WHEN 조건1 THEN A
			WHEN 조건2 THEN B
	 ELSE 'C'
   END (AS RESULT)

"""
2023 02 16

 
1. 집계함수의 대한 이해

2.특수함수

-connecby

-partition by

-rank

-groupconcat

if
"""
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
Group by 

1. group by 를 쓸때 각 매출을 구하고 싶다면 이와 같이 구하기
(매출 = 수량 x  가격)

EX1) SUM( PRICE * SALE) (OK)

EX2) (PRICE * SUM(SALE) (X)

Rank() over(order by desc) as rnk

후 n번째로 할꺼면 서브쿼리로 맏늘어서 구하면됨!



Join 정리도 필요

Left join

right join

case nullif dateformat if

04.28 부터 문풀이


# Group by

1. 자동차 대여 기록에서 대여중 대여가능 여부 구분하기

-> 
select id , (
    case
        when number = 1 then 'true'
        when number = 2 then 'flase'
    else 'not'
end
)as ck