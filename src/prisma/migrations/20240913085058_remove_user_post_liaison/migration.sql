/*
  Warnings:

  - You are about to drop the column `author_id` on the `Post` table. All the data in the column will be lost.

*/
-- DropForeignKey
ALTER TABLE "Post" DROP CONSTRAINT "Post_author_id_fkey";

-- DropIndex
DROP INDEX "Post_author_id_key";

-- AlterTable
ALTER TABLE "Post" DROP COLUMN "author_id";
