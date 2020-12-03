import config.{ConfigurationParser, CountConfig}
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions.col
import org.slf4j.{Logger, LoggerFactory}


object GroupedCount {
  def main(args: Array[String]): Unit = {
    val logger: Logger = LoggerFactory.getLogger(this.getClass)

    logger.info("Reading configuration")
    val config: CountConfig = ConfigurationParser.readJobArguments(args)

    logger.info("Building Spark Session")
    val ss = SparkSession
      .builder()
      .appName(config.appName)
      .getOrCreate()

    logger.info("Reading CSV")
    val inputData = ss
      .read
      .option("header", "true")
      .option("inferSchema", "true")
      .csv(config.csvPath)

    inputData.groupBy(col(config.groupColumn)).count().write.csv(config.outputPath)
  }
}
