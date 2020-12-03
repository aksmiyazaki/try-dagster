#!/bin/bash

echo "========================================================================="
echo
echo "   Atenção: esse script deve ser utilizado apenas para fins de teste"
echo "            a app inicializada deve ser killadas após o teste."
echo "            A execução das apps de stream do horizon devem ser"
echo "            inicializadas usando o projeto spark-monit "
echo
echo "========================================================================="

if ["$SPARK_HOME" == ""] || ["$HADOOP_USER_NAME" == ""] || ["$HADOOP_CONF_DIR" == ""]; then
    echo 'Missing Environment variable: export your locals.'
    exit 1
fi;

$SPARK_HOME/bin/spark-submit -v \
--master yarn-cluster \
--driver-memory 1g \
--executor-memory 1g \
--executor-cores 1 \
--num-executors 1 \
--driver-java-options "-Dhdp.version=2.6.5.0-292 -Dglake.service.address=http://glake-api-qa.gcloud.dev.globoi.com" \
--conf "spark.executor.extraJavaOptions=-XX:+UseG1GC" \
--conf spark.eventLog.enabled=false \
--conf spark.eventLog.dir=hdfs:///logs/spark \
--conf spark.eventLog.overwrite=true \
--conf spark.yarn.maxAppAttempts=1 \
--conf spark.yarn.submit.waitAppCompletion=true \
--conf spark.hadoop.yarn.timeline-service.enabled=false \
--conf spark.sql.broadcastTimeout=200000 \
--class GroupedCount \
../target/scala-2.11/grouped-csv-count.jar \
--app-name CountCSV \
--input-csv-path /tmp/aksmiyazaki/dummy.csv \
--group-column name \
--output-data-path /tmp/aksmiyazaki/result \
"$@"