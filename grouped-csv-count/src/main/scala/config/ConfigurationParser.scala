package config
import scopt.OParser

//noinspection ScalaStyle
object ConfigurationParser {
  def readJobArguments(args: Array[String]): CountConfig = {
    val builder = OParser.builder[CountConfig]
    import builder._

    val metadataParser = OParser.sequence(
      programName("ObjectMetadata_Merge"),
      head("scopt", "4.x"),
      opt[String]('a', "app-name").action((x, c) => c.copy(appName = x))
        .text("Name of the application").required(),
      opt[String]('i', "input-csv-path").action((x, c) => c.copy(csvPath = x))
        .text("Location of CSV to be read").required(),
      opt[String]('c', "group-column").action((x, c) => c.copy(groupColumn = x))
        .text("Column to group by."),
      opt[String]('o', "output-data-path").action((x, c) => c.copy(outputPath = x))
        .text("HDFS directory to write output data."))

    OParser.parse(metadataParser, args, CountConfig()) match {
      case Some(config) =>
        config
      case _ =>
        throw new IllegalArgumentException("Cannot parse your configurations, " +
          "make sure that you passed the required parameters correctly.")
    }
  }
}
