--No of Hashmapper having skill set for that particular Role
SELECT DISTINCT "Skills Bucket", count(distinct "Consultant Name") FROM  SRIKANT.HASHMAP_SKILLS_REPO_SKILLS WHERE "Skills Bucket" IS NOT NULL GROUP BY 1 ORDER BY 2 desc;


--No of Hashmapper knowing that particular tool/tech
SELECT "Skill Sets", count(*) FROM SRIKANT.HASHMAP_SKILLS_REPO_SKILLS WHERE "Skill Sets" IS NOT NULL GROUP BY 1 ORDER BY 2 desc;


--No of Hashmapper in a project
select  COALESCE("Current Active Project", 'Internl Tech Team(ITT)'), count(distinct "Consultant Name") FROM SRIKANT.HASHMAP_SKILLS_REPO_SKILLS
group by 1 ORDER BY 2 DESC;


--No of Hashmapper in a project for that Role
select  "Current Active Project", "Skills Bucket",  count(distinct "Consultant Name") FROM SRIKANT.HASHMAP_SKILLS_REPO_SKILLS WHERE "Current Active Project" IS NOT null
group by 1, 2 ORDER BY 3, 1  ;


--No of certifications and unique skills of a hashmapper
SELECT  count(DISTINCT "Certifications Completed"), "Consultant Name", count(DISTINCT "Skill Sets") FROM SRIKANT.HASHMAP_SKILLS_REPO_SKILLS  GROUP BY 2;


--Name of hashmapper with no skills
SELECT DISTINCT "Consultant Name" FROM  SRIKANT.HASHMAP_SKILLS_REPO_SKILLS WHERE "Skill Sets" IS NULL;
