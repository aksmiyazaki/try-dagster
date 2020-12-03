import sbt.{ExclusionRule, _}

object Dependencies {

  val sparkVersion = "2.4.4"
  val providedDependencies = Seq(
    "org.apache.spark" %% "spark-core"      % sparkVersion exclude("org.scalatest", "scalatest"),
    "org.apache.spark" %% "spark-sql"       % sparkVersion,
    "org.apache.spark" %% "spark-yarn"      % sparkVersion
  ).map(_.excludeAll(ExclusionRule("org.scalatest", "scalatest_2.11")))

  val testsDependencies = Seq(
    "org.scalatest"     %% "scalatest"                   % "3.0.5",
    "org.scalamock"     %% "scalamock-scalatest-support" % "3.6.0",
    "com.holdenkarau"   %% "spark-testing-base"          % s"${sparkVersion}_0.14.0",
    "org.apache.spark"  %% "spark-hive"                  % sparkVersion
  )

  val organizationsToExclude = testsDependencies.map(_.organization).filter(!_.contains("spark")).map(org => ExclusionRule(organization = org))

  val embeddedDependencies = Seq(
    "com.github.scopt"            %% "scopt"                   % "4.0.0-RC2"
  ).map(_.excludeAll(organizationsToExclude: _*))

  val rootDependencies = embeddedDependencies ++ providedDependencies.map(_ % Provided) ++ testsDependencies.map(_ % Test)

  val mainRunnerDependencies = (embeddedDependencies ++ providedDependencies ++ testsDependencies).map(_ % Compile)

}
